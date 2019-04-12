from django.contrib.auth.models import User
from django.db import models


class UserAccount(User):
    address = models.CharField(max_length=355, blank=False)
    house_address = models.CharField(max_length=344, blank=True)

    def __str__(self):
        return self.email

