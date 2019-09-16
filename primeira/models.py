from django.db import models
from django.db import IntegrityError

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome

class CarrinhoDeCompras(models.Model):
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(CarrinhoDeCompras, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
