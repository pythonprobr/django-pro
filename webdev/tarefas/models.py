from django.db import models


# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(max_length=128)
    feita = models.BooleanField(default=False)
