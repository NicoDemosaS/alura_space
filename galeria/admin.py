from django.contrib import admin
from galeria.models import Fotografia
# Register your models here.


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicado")
    list_display_links = ("id", "nome",)
    search_fields = ("nome",)
    list_editable = ("publicado",)
    list_filter = ("categoria", "usuario",)

admin.site.register(Fotografia, ListandoFotografias)