import os
from django.contrib.gis.utils import LayerMapping
from .models import Restaurant

world_mapping = {
    #'serial' : 'S.no',
    'restaurant' : 'restaurant',
    'rating' : 'rating',
    'type' : 'Type',
    'cuisines' : 'Cuisines',
    'cost' : 'Cost',
    'address' : 'address',
    'features' : 'features',
    'latitude' : 'latitude',
    'longitude' : 'longitude',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'resturent.shp'),
)

#world_shp = os.path.join(os.path.dirname(__file__), "data", 'TM_WORLD_BORDERS-0.3.shp').decode("DOS/OS2-852").encode("utf-8")


def run(verbose=True):
    lm = LayerMapping(Restaurant, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


