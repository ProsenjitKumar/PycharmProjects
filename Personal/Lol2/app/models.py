from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


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

    point = models.PointField(default='POINT(0.0 0.0)')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant


class Restaurant1(models.Model):
    restaurant = models.CharField(max_length=254)
    rating = models.FloatField()
    type = models.CharField(max_length=254)
    cuisines = models.CharField(max_length=254)
    cost = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    features = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()

    point = models.PointField(default='POINT(0.0 0.0)')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant

