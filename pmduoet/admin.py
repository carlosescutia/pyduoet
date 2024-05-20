from django.contrib import admin

# Register your models here.

from .models import Municipio
from .models import Documento
from .models import Avance

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    pass

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_filter = ('municipio',)

@admin.register(Avance)
class AvanceAdmin(admin.ModelAdmin):
    list_filter = ('tipo', 'status', 'municipio',)
