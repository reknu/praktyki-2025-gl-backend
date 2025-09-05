from django.db import models

class Parking(models.Model):
    spot_number = models.CharField(max_length=10)
    floor = models.IntegerField()
    status = models.IntegerField()