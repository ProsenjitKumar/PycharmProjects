import os
from django.contrib.gis.utils import LayerMapping
from .models import Birds

world_mapping = {
    #'serial' : 'S.no',
    'kingdom' : 'Kingdom',
    'phylum' : 'Phylum',
    'bird_class' : 'Class',
    'order' : 'Order',
    'family' : 'Family',
    'family_author' : 'Author',
    'genus' : 'Genus',
    'genus_author' : 'Author_1',
    'scientific_name' : 'Scientific',
    'scientific_name_author' : 'Author_2',
    'year': 'Year',
    'status': 'Status',
    'accepted_as': 'Accepted a',
    'bengali_name': 'Bengali Na',
    'english_name': 'English Na',
    'size_cm': 'Size (cm)',
    'common_family': 'Common Fam',
    'common_group': 'Common Gro',
    'habit': 'Habit',
    'conservation_status': 'Conservati',
    'distribution_in_bengal': 'Distributi',
    'reference': 'References',

}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'birds_shape', 'birds.shp'),
)


def run(verbose=True):
    lm = LayerMapping(Birds, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


