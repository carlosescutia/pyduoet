from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Municipio(models.Model):
    cve_mun = models.CharField(max_length=3, default=None, blank=True, null=True)
    nom_mun_corto = models.CharField(max_length=50, default=None, blank=True, null=True)
    nom_mun_largo = models.CharField(max_length=200, default=None, blank=True, null=True)
    img_mun = models.ImageField(upload_to='img/img_mun', default=None, blank=True, null=True)

    @property
    def img_mun_url(self):
        if self.img_mun and hasattr(self.img_mun, 'url'):
            return self.img_mun.url

    def __str__(self):
        return f"{self.cve_mun} {self.nom_mun_corto}"

    class Meta:
        ordering = ['cve_mun']


class Documento(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    etiqueta = models.TextField(default=None, blank=True, null=True)
    url = models.TextField(default=None, blank=True, null=True)
    archivo = models.FileField(upload_to='docs', default=None, blank=True, null=True)
    posicion = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.municipio.cve_mun} {self.municipio.nom_mun_corto} - {self.posicion} - {self.etiqueta}"

    class Meta:
        ordering = ['municipio', 'posicion']

class Avance(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    nombre = models.TextField(max_length=200, default=None, blank=True, null=True)
    TIPO_AVANCE = (
            ('parcial', 'Programa parcial'),
            ('municipal', 'Programa municipal'),
            )
    tipo = models.TextField(
        max_length=20,
        choices=TIPO_AVANCE,
        blank=True,
        default='municipal',
        help_text='Tipo de avance',
        )
    STATUS_AVANCE = (
            ('diagnostico', 'Diagnóstico'),
            ('elaboracion', 'Elaboración'),
            ('dictaminacion', 'Dictaminación'),
            ('revision', 'Revisión'),
            ('dictaminado', 'Dictaminado'),
            ('publicado', 'Publicado'),
            ('pendiente', 'Pendiente'),
            )
    status = models.TextField(
        max_length=20,
        choices=STATUS_AVANCE,
        blank=True,
        default='diagnostico',
        help_text='Status del avance',
        )
    dictaminacion = models.DateField(default=None, null=True, blank=True)
    publicacion = models.DateField(null=True, blank=True)
    comentarios = models.TextField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        """String for representing the Avance object (in Admin site etc.)"""
        return f'{self.municipio.nom_mun_corto} ({self.tipo}) - {self.status}'
