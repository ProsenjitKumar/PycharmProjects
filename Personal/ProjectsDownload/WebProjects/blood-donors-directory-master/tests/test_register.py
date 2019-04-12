from uuid import UUID
from bdd import models
from datetime import date
from django.test import TestCase


class RegisterTestCase(TestCase):
    def setUp(self):
        self.blood_group = models.BloodGroup.objects.create(name="A+")
        self.donor = models.Donor.objects.create(blood_group=self.blood_group, first_name="Akhil", last_name="Lawrence")
        self.register = models.Register.objects.create(donor=self.donor, comment="this-is-a-comment", donation_date=date.today())

    def test_id(self):
        self.assertIsInstance(self.blood_group.id, UUID)
