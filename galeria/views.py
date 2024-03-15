from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografias
# Create your views here.



def index(request):
    fotografias = Fotografias.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias} )

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografias, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})