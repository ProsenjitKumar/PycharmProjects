from rest_framework import serializers

from . import models


class BloodGroup(serializers.ModelSerializer):
    """ serializer for the blood group model """
    class Meta(object):
        model = models.BloodGroup
        fields = "__all__"


class Donor(serializers.ModelSerializer):
    """ serializer for the donor model """
    class Meta(object):
        model = models.Donor
        fields = "__all__"


class Register(serializers.ModelSerializer):
    """ serializer for the register model """
    class Meta(object):
        model = models.Register
        fields = "__all__"
