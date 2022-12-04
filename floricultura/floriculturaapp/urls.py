from django.urls import path, include

from floriculturaapp import views


urlpatterns = [
    path('produto', views.ListaDeProdutos.as_view()),
    path('carrinho', views.ListaDeCarrinho.as_view()),
    path('carrinho/<int:id>', views.ListaDeCarrinho.as_view()),
    path('compra/finalizar', views.Compra.as_view()),
]