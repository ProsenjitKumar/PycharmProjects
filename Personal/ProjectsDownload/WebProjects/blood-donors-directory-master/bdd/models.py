from __future__ import unicode_literals

import uuid
from datetime import datetime

from django.db import models


class Base(models.Model):
    """ base class for all models """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_on = models.DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        abstract = True


class BloodGroup(Base):
    """ model representing the blood group """
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Donor(Base):
    """ model representing the donor """
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name

    def __unicode__(self):
        return self.full_name


class Register(Base):
    """ model representing the register """
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    comment = models.TextField()
    donation_date = models.DateField()

    @property
    def is_available(self):
        today = datetime.today()
        if (today - self.donation_date) > 90:
            return True
        return False

    def __str__(self):
        return self.donor.full_name

    def __unicode__(self):
        return self.donor.full_name
