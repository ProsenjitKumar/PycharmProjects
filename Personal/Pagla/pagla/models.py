#from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Restaurant(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    #serial = models.CharField(max_length=254)
    restaurant = models.CharField(max_length=254)
    rating = models.FloatField()
    type = models.CharField(max_length=254)
    cuisines = models.CharField(max_length=254)
    cost = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    features = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.restaurant

