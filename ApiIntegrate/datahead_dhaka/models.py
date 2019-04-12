from django.db import models
from django.utils.text import slugify

class Passenger(models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=20)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=300)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Passenger, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
