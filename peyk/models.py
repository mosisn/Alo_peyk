from django.db import models
from django.contrib.auth.models import User


class Origin(models.Model):
    city = models.CharField(("Tehran"), max_length=50)
    address = models.TextField()
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)                
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return "{}".format(self.address)


class Destination(models.Model):
    origin = models.ManyToManyField(Origin)
    city = models.CharField(("Tehran"), max_length=50)
    address = models.TextField()
    name = models.CharField( max_length=50)
    phone_number = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return "{}".format(self.address)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT)
    destination = models.ManyToManyField(Destination)
    duration  = models.CharField( max_length=50)
    price = models.CharField( max_length=50)
    tracking_code = models.CharField( max_length=5)

    def __str__(self) -> str:
        return "{} - {}".format(self.user,self.No)