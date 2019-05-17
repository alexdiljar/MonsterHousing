from django.db import models
from django.contrib.auth.models import User
from Properties.models import Properties
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


class CreditCard(models.Model):
    cc_number = models.CharField(max_length=16)
    cc_month = models.CharField(max_length=2)
    cc_year = models.CharField(max_length=2)
    cc_code = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
class Transactions(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_date = models.DateField(auto_now_add=True, blank=True)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
