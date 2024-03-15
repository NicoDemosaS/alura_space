from django.db import models

# Create your models here.

class Fotografias(models.Model):
    pass
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(blank=False)
    legenda = models.CharField(max_length=50, null=False, blank=False)
    foto = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'Fotografia {self.nome}'