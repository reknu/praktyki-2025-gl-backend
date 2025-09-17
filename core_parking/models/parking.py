from django.db import models

class Parking(models.Model):
    class Status(models.IntegerChoices):
        FREE = 0, 'FREE'
        OCCUPIED = 1, 'OCCUPIED'
    spot_number = models.CharField(max_length=10)
    floor = models.IntegerField()
    status = models.IntegerField(choices=Status.choices, default=Status.FREE)
    aisle = models.CharField(max_length=40)