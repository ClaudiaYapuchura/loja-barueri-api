from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255) 
    telefone = models.CharField(max_length=13)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    data_nascimento = models.CharField(max_length=10) 
    idade = models.IntegerField()