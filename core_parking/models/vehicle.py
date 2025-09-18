from django.db import models
from .user import User

class Vehicle(models.Model):
    registration_number = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    