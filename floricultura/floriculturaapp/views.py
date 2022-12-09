import json
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Produto
from .models import Carrinho
from .models import Usuario
from .models import ProdutoHistoricoCompras
from .models import HistoricoCompras
from .serializers import ProdutoSerializer
from .serializers import CarrinhoSerializer
from .serializers import HistoricoComprasSerializer
from rest_framework.response import Response
import requests
import logging

# Create your views here.

from django.http import HttpResponse


class ListaDeProdutos(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

class ListaDeCarrinho(APIView):
    def get(self, request):
        carrinho = Carrinho.objects.all()
        serializer = CarrinhoSerializer(carrinho, many=True)
        return Response(serializer.data)
    def post(self, request):
        usuario = Usuario.objects.get(id=request.POST.get('idUsuario'))
        produto = Produto.objects.get(id=request.POST.get('idProduto'))
        Carrinho.objects.create(quantidade=request.POST.get('quantidade'), idProduto=produto, idUsuario=usuario)
        return Response('ok')
    def delete(self, request, id):
        Carrinho.objects.filter(id=id).delete()
        return Response('ok')

    def put(self, request, id):
        carrinho = Carrinho.objects.get(id=id)
        carrinho.quantidade = request.POST.get('quantidade')
        carrinho.save()
        return Response('ok')

class ListaHistoricoCompras(APIView):
    def get_last(self):
        historico = HistoricoCompras.objects.last()
        serializer = HistoricoComprasSerializer(historico)
        return serializer.data
    
    def post(self, data):
        HistoricoCompras.objects.create(valor_total= data["valor_total"])
        return Response('ok')

class Compra(APIView):
    def post(self, request):
        data = request.body.decode()
        data1 = json.loads(data)
        if self.envia_dados_pagamento_pagseguro(data) == "201":
            lista = ListaHistoricoCompras()
            lista.post(data={"valor_total": data1["charges"][0]["amount"]["value"]})
            ultima_compra = lista.get_last()
            for i in data1["items"]:
                produto_id = Produto.objects.get(id=i["reference_id"])
                historico_compra = HistoricoCompras.objects.get(id=ultima_compra['id'])
                ProdutoHistoricoCompras.objects.create(quantidade=i["quantity"], idProduto=produto_id, idHistoricoCompras=historico_compra)
            response = "sucesso"
        else:
            response = "error"
        return Response(response)

    def envia_dados_pagamento_pagseguro(self, data_dict):
        response = requests.post('https://sandbox.api.pagseguro.com/orders', data=data_dict, headers={'Authorization': 'Bearer 540CD5FAE4074E4D87F9BA20A897A93E','Content-Type': 'application/json', 'Accept': 'application/json'})
        return str(response.status_code)



