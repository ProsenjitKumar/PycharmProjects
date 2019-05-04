from django.db import models


class ClientCompany(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    place = models.CharField(max_length=500, db_index=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
