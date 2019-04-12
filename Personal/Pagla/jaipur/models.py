#from django.db import models
from django.contrib.gis.db import models
#from django.contrib.gis.geos import Point


class Restaurant(models.Model):
    restaurant = models.CharField(max_length=254)
    rating = models.FloatField()
    type = models.CharField(max_length=254)
    cuisines = models.CharField(max_length=254)
    cost = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    features = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()

    mpoly = models.PointField()

    def __str__(self):
        return self.restaurant

