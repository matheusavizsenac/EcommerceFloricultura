from rest_framework import serializers

from .models import Produto
from .models import Carrinho

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
        "id",
        "nome",
        "descricao",
        "preco",
        "imagem"
        )

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = (
        "id",
        "idProduto",
        "idUsuario",
        "quantidade"
        )
        depth = 1