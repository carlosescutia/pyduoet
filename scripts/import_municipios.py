# import_municipios.py
from pmduoet.models import Municipio
import csv

def import_municipios(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Municipio.objects.create(
                    cve_mun=row['cve_mun'],
                    nom_mun_corto=row['nom_mun_corto'],
                    nom_mun_largo=row['nom_mun_largo'],
                    img_mun=row['img_mun'],
                    )

def run():
    csv_file_path = '/usr/src/app/scripts/municipios.csv'
    import_municipios(csv_file_path)
