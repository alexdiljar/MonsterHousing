from django.db import models

# Create your models here.
class Search(models.Model):
    country = models.CharField(max_length=255)
    zip = models.IntegerField()
    type = models.CharField(max_length=999)
    tags = models.CharField(max_length=999)
    size = models.CharField(max_length=255)
    price = models.FloatField()
    rooms = models.IntegerField()