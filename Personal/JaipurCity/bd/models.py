from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Bd(models.Model):
    name = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()

    point = models.PointField()

    def __str__(self):
        return self.name



class Hospital2(models.Model):
    hospital_n = models.CharField(max_length=255)
    hospital_r = models.FloatField()
    contact_nu = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    point = models.PointField()

    def __str__(self):
        return self.hospital_n
