from django.db import models

# Create your models here.
class Search(models.Model):
    country = models.CharField(max_length=255,null=True)
    zip = models.IntegerField(null=True)
    type = models.CharField(max_length=999,null=True)
    tags = models.CharField(max_length=999,null=True)
    size = models.CharField(max_length=255,null=True)
    price = models.FloatField(null=True)
    rooms = models.IntegerField(null=True)