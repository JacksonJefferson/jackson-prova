from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class CarrinhoDeCompras(models.Model):
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=1)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
