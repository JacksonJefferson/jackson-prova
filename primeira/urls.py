from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('produto/', views.produto_list),
    path('produto/<int:produto_id>', views.produto_show),
    path('produto/create/', views.produto_form),
    path('produto/delete/<int:produto_id>/', views.produto_delete),
    path('produto/editar/<int:produto_idd>', views.produto_editar),
    path('cliente/', views.cliente_list),
    path('cliente/create/', views.cliente_form),
    path('carrinho/', views.carrinho_list),
    path('carrinho/create/', views.carrinho_form),
]