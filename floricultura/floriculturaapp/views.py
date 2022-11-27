from django.shortcuts import render
from rest_framework.views import APIView
from .models import Produto
from .models import Carrinho
from .models import Usuario
from .serializers import ProdutoSerializer
from .serializers import CarrinhoSerializer
from rest_framework.response import Response
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
