import os
from django.contrib.gis.utils import LayerMapping
from .models import Hospital2

world_mapping = {
    #'serial' : 'S.no',
    'hospital_n' : 'hospital_n',
    'hospital_r' : 'hospital_r',
    'contact_nu' : 'contact_nu',
    'address' : 'address',
    'latitude' : 'latitude',
    'longitude' : 'longitude',
    'point' : 'POINT',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'hospital', 'hospitals.shp'),
)


def run(verbose=True):
    lm = LayerMapping(Hospital2, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


