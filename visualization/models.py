from django.db import models

class Linha(models.Model):
    codigo_atual = models.CharField(default="", max_length=256)
    nome_atual = models.CharField(default="", max_length=256)
    novo_nome = models.CharField(default="", max_length=256)
    proposta = models.CharField(default="", max_length=256)
