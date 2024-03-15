from django.db import models
from datetime import datetime
# Create your models here.

class Fotografia(models.Model):
    
    categorias = [ 
    ("NEBULOSA", "Nebulosa"),
    ("GALAXIA", "Galaxia"),
    ("ESTRELAS", "Estrela"),
    ("CACHORRINHOS!", "AUAU"),
]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    legenda = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=categorias, default='', blank=False, null=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia {self.nome}'