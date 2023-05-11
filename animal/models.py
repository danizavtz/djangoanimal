from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    especie  = models.CharField(max_length=20)
