from uuid import UUID

from django.test import TestCase
from freezegun import freeze_time

from bdd import models, serializers


@freeze_time("2017-04-29")
class BloodGroupTestCase(TestCase):

    def setUp(self):
        self.blood_group = models.BloodGroup.objects.create(name="A+")

    def test_id(self):
        self.assertIsInstance(self.blood_group.id, UUID)

    def test_name(self):
        self.assertEquals(self.blood_group.name, "A+")

    def test_print_object(self):
        self.assertEquals(str(self.blood_group), "A+")

    def test_serialization(self):
        data = serializers.BloodGroup(self.blood_group).data
        expected_data = {
            "id": str(self.blood_group.id),
            "name": "A+",
            "created_on": "2017-04-29T00:00:00",
            "last_modified_on": "2017-04-29T00:00:00"
        }
        self.assertDictEqual(data, expected_data)
