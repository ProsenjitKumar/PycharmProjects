from uuid import UUID
from bdd import models
from django.test import TestCase


class DonorTestCase(TestCase):
    def setUp(self):
        self.blood_group = models.BloodGroup.objects.create(name="A+")
        self.donor = models.Donor.objects.create(blood_group=self.blood_group, first_name="Akhil", last_name="Lawrence")

    def test_id(self):
        self.assertIsInstance(self.blood_group.id, UUID)

    def test_donor(self):
        self.assertEquals(self.donor.first_name, "Akhil")

    def test_last_name(self):
        self.assertEquals(self.donor.last_name, "Lawrence")

    def test_full_name(self):
        self.assertEquals(self.donor.full_name, "Akhil Lawrence")

    def test_print_object(self):
        self.assertEquals(str(self.donor), "Akhil Lawrence")
