from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50)

    @property
    def city(self):
        return self.city()


class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)


class Origin(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    address = models.TextField()
    name = models.CharField( max_length=50)
    phone_number = models.CharField(max_length=50)
    No =models.CharField( max_length=4)
    Unit = models.CharField( max_length=3)                  
    description = models.TextField()


class Destination(models.Model):
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    address = models.TextField()
    name = models.CharField( max_length=50)
    phone_number = models.CharField(max_length=50)
    No =models.CharField( max_length=4)
    Unit = models.CharField( max_length=3)
    description = models.TextField()


class Order(models.Model):
    # User = 
    # driver =
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT)
    destination = models.ManyToManyField(Destination)
    duration  = models.CharField( max_length=50)
    price = models.CharField( max_length=50)
    No = models.CharField( max_length=5)
