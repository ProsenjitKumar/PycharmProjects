from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from . import models, serializers


class CrudAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    """ generic api which is able to perform read, write, update and delete """
    def get(self, request, *args, **kwargs):
        if self.lookup_field in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class BloodGroupAPIView(CrudAPIView):
    """ api to perform crud operations on the blood group model """
    queryset = models.BloodGroup.objects.all()
    serializer_class = serializers.BloodGroup


class DonorAPIView(CrudAPIView):
    """ api to perform crud operations on the donor model """
    queryset = models.Donor.objects.all()
    serializer_class = serializers.Donor


class RegisterAPIView(CrudAPIView):
    """ api to perform crud operations on the register model """
    queryset = models.Register.objects.all()
    serializer_class = serializers.Register
