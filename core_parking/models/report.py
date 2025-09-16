from django.db import models
from .parking import Parking
from .employee import Employee 

class Report(models.Model):
    reporter = models.ForeignKey(Employee, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(Parking, on_delete=models.CASCADE)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Zgłoszenie od {self.reporter.first_name} {self.reporter.last_name} dla miejsca {self.parking_spot.spot_number}"