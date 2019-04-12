from django.contrib import admin

from . import models

admin.site.register(models.BloodGroup)
admin.site.register(models.Donor)
admin.site.register(models.Register)
