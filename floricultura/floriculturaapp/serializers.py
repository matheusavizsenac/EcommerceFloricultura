from rest_framework import serializers

from .models import Produto
from .models import Carrinho
from .models import HistoricoCompras

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

class HistoricoComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoCompras
        fields = (
            "id",
            "valor_total"
        )