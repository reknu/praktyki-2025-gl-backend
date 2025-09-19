from django.contrib import admin
from .models import Vehicle, Parking, Reservation, Employee , User

admin.site.register(Vehicle)
admin.site.register(Parking)
admin.site.register(Reservation)
admin.site.register(Employee)
admin.site.register(User)