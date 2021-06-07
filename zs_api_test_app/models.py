from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=200)
    house_no = models.CharField(max_length=200)
    road_no = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.house_no + self.road_no

