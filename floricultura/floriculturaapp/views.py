import json
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Produto
from .models import Carrinho
from .models import Usuario
from .serializers import ProdutoSerializer
from .serializers import CarrinhoSerializer
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


class Compra(APIView):
    def post(self, request):
        data2 = {"reference_id":"zqp2zhf295","customer":{"name":"Matheus Aviz","email":"email@test.com","tax_id":"12345678909","phones":[{"country":"55","area":"11","number":"999999999","type":"MOBILE"}]},"items":[{"reference_id":4,"name":"Planta","quantity":1,"unit_amount":30},{"reference_id":4,"name":"Planta","quantity":1,"unit_amount":30},{"reference_id":4,"name":"Planta","quantity":1,"unit_amount":30},{"reference_id":4,"name":"Planta","quantity":1,"unit_amount":30}],"qr_code":{"amount":{"value":500}},"shipping":{"address":{"street":"General","number":"288","complement":"Casa","locality":"Velha","city":"Blumenau","region_code":"SC","country":"BRA","postal_code":"89041000"}},"notification_urls":["https://meusite.com/notificacoes"],"charges":[{"reference_id":"referencia do pagamento","description":"descricao do pagamento","amount":{"value":120,"currency":"BRL"},"payment_method":{"type":"CREDIT_CARD","installments":1,"capture":"true","card":{"number":"4111111111111111","exp_month":"12","exp_year":"2026","security_code":"123","holder":{"name":"Jose Da Silva"},"store":"false"}},"notification_urls":["https://meusite.com/notificacoes"]}]}
        ##data1 = request.body.decode()
        print(type(data2))
        ##print(type(data1))
        ##print(data1)
        response = self.envia_dados_pagamento_pagseguro(data2)
        return Response(response)

    def envia_dados_pagamento_pagseguro(self, data):
        response = requests.post('https://sandbox.api.pagseguro.com/orders', json=data, headers={'Authorization': 'Bearer 540CD5FAE4074E4D87F9BA20A897A93E','Content-Type': 'application/json', 'Accept': 'application/json'})
        print("status code: " + str(response.content))



