from django.shortcuts import render

# Create your views here.

fotografias = [
    {"nome": "Nebula PeipipiPOPOPOPO"}
]

def index(request):
    return render(request, 'galeria/index.html', {"cards": fotografias} )

def imagem(request):
    return render(request, 'galeria/imagem.html')