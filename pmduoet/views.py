from django.shortcuts import render
from django.views import generic
from .models import Municipio, Avance
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    """View function for home page of site."""

    # generar lista de Municipios
    municipio_list = Municipio.objects.all()

    # "municipio" mapa
    mapa = Municipio.objects.filter(cve_mun='200').first()

    # Ultima actualizacion
    ultima_actualizacion = Avance.objects.latest('actualizado').actualizado

    context = {
            'municipio_list': municipio_list,
            'mapa': mapa,
            'ultima_actualizacion': ultima_actualizacion,
            }

    return render(request, 'index.html', context=context)
