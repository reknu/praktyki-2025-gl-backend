from django.db import models

from . import Vehicle
from .user import User
from .parking import Parking

class Reservation(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey(Parking, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)