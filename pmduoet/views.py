from django.shortcuts import render
from django.views import generic
from .models import Municipio

# Create your views here.

def index(request):
    """View function for home page of site."""

    # generar lista de Municipios
    municipio_list = Municipio.objects.all()

    context = {
            'municipio_list': municipio_list,
            }

    return render(request, 'index.html', context=context)
