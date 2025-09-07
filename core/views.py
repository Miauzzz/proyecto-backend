from django.shortcuts import render
from .models import Noticia
from .models import Inicio
from .models import Herramienta

# Create your views here.

def inicio(request):
    inicio = Inicio.objects.all()
    herramientas = Herramienta.objects.all()
    return render(request, 'core/inicio.html', {'inicio': inicio, 'herramientas': herramientas})

def noticias(request):
    noticias = Noticia.objects.order_by('-fecha_publicacion')
    return render(request, 'core/noticias.html', {'noticias': noticias})

def herramientas(request):
    herramientas = Herramienta.objects.all()
    return render(request, 'core/herramientas.html', {'herramientas': herramientas})

def nosotros(request):
    return render(request, 'core/nosotros.html')