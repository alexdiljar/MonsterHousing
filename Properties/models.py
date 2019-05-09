from django.db import models


# Create your models here.
class Cities(models.Model):
    country = models.CharField(max_length=255)
    zip = models.IntegerField()
    city = models.CharField(max_length=255)


class Addresses(models.Model):
    street = models.CharField(max_length=255)
    house_no = models.IntegerField()
    Cities = models.ForeignKey(Cities, on_delete=models.CASCADE)


class Tags(models.Model):
    elevator = models.BooleanField()
    garage = models.BooleanField()
    near_bloodbank = models.BooleanField()
    dungeon = models.BooleanField()
    seacret_entrence = models.BooleanField()


class Types(models.Model):
    description = models.CharField(max_length=999)


class Details(models.Model):
    T_ID = models.ForeignKey(Tags, on_delete=models.CASCADE)
    Ty_ID = models.ForeignKey(Types, on_delete=models.CASCADE)
    size = models.CharField(max_length=255)
    price = models.FloatField()
    rooms = models.IntegerField()
    description = models.CharField(max_length=999)
    property_image = models.CharField(max_length=999)


class Properties(models.Model):
    pass
