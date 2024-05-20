from django.shortcuts import render
from django.views import generic
from .models import Municipio
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    """View function for home page of site."""

    # generar lista de Municipios
    municipio_list = Municipio.objects.all()

    context = {
            'municipio_list': municipio_list,
            }

    return render(request, 'index.html', context=context)
