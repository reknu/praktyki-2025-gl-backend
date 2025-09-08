from django.db import models

class Parking(models.Model):
    STATUS_CHOICES = (
        ('FREE', 'FREE'),
        ('OCCUPIED', 'OCCUPIED'),
    )

    spot_number = models.CharField(max_length=10)
    floor = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='FREE')

    def __str__(self):
        return self.spot_number