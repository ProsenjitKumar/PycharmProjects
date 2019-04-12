from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos


class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    location = gis_models.PointField(u"longitude/latitude",
                                     geography=True, blank=True, null=True)

    gis = gis_models.PointField
    objects = models.Manager()

    def __str__(self):
        return self.name
