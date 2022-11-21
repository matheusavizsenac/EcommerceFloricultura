from django.shortcuts import render
from rest_framework.views import APIView
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.response import Response
# Create your views here.

from django.http import HttpResponse


class ListaDeProdutos(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
