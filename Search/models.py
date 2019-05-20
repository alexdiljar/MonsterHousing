from django.db import models
from django.contrib.auth.models import User
from Properties.models import Properties


# Create your models here.
class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #property = models.ForeignKey(Properties, on_delete=models.CASCADE)




    #country = models.CharField(max_length=255, blank=True, null=True)
    #zip = models.IntegerField(blank=True, null=True)
    # type = models.CharField(max_length=999, blank=True)
    # tags = models.CharField(max_length=999, blank=True)
    # size = models.CharField(max_length=255, blank=True)
    # price = models.FloatField(blank=True, null=True)
    # rooms = models.IntegerField(blank=True, null=True)
    #sort = models.CharField(max_length=255, blank=True)
    # search = models.CharField(max_length=255, blank=True, null=True)
