from django.db import models

# Create your models here.

class Endereco(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    rua = models.CharField(max_length=100, null=False)
    bairro = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=10, null=False)
    complemento = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.id, self.rua)

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=100, null=False)
    senha = models.CharField(max_length=50, null=False)
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.id, self.nome)

class Produto(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=100)
    preco = models.FloatField(null=False)
    imagem = models.ImageField()

    def __str__(self):
        return "{} - {}".format(self.id, self.nome)

class HistoricoCompras(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    valor_total = models.FloatField(null=False)
    data_compra = models.DateField(auto_now=True)
    compras = models.ManyToManyField(Produto, related_name='historico', through='ProdutoHistoricoCompras')

    def __str__(self):
        return "{} - {}".format(self.id, self.data_compra)

class ProdutoHistoricoCompras(models.Model):
    quantidade = models.IntegerField(null=False)
    idProduto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="produto_historico")
    idHistoricoCompras = models.ForeignKey(HistoricoCompras, on_delete=models.CASCADE, related_name="produto_historico")


class Carrinho(models.Model):
    quantidade = models.IntegerField(null=False)
    idProduto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="carrinho_produto")
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="carrinho_usuario")