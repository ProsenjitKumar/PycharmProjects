import os
from django.contrib.gis.utils import LayerMapping
from .models import PoliceStation

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)

#world_shp = os.path.join(os.path.dirname(__file__), "data", 'TM_WORLD_BORDERS-0.3.shp').decode("DOS/OS2-852").encode("utf-8")


def run(verbose=True):
    lm = LayerMapping(PoliceStation, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


