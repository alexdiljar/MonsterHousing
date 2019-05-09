from django.db import models
from django.contrib.auth.models import User
from Properties.models import Addresses


class Profile(models.Model):
    ssn = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=999)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
