from django.db import models
from django.contrib.auth.models import User
from Properties.models import Properties


# Create your models here.
class Transactions(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateField(auto_now=True)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
