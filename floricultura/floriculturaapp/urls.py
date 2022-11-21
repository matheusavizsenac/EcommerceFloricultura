from django.urls import path, include

from floriculturaapp import views


urlpatterns = [
    path('', views.ListaDeProdutos.as_view()),
]