from django.db import models

class Vehicle(models.Model):
    registration_number = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)