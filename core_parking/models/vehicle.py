from django.db import models
from .user import User

class Vehicle(models.Model):
    registration_number = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
def __str__(self):
    return f"{self.registration_number} - {self.brand} {self.model}"