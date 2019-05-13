from django.db import models
from django.contrib.auth.models import User
from Properties.models import Properties, Addresses


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=999)

