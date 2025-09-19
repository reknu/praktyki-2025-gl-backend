from django_filters import rest_framework as filters
from .models import Vehicle, Parking, Reservation
ALLOWED_BRANDS_CHOICES = [
    ("Toyota", "Toyota"), ("Nissan", "Nissan"), ("BMW", "BMW"),
    ("Volkswagen", "Volkswagen"), ("Mercedes", "Mercedes"), ("Suzuki", "Suzuki"),
]

class VehicleFilter(filters.FilterSet):
    brand = filters.ChoiceFilter(choices=ALLOWED_BRANDS_CHOICES)

    class Meta:
        model = Vehicle
        fields = ['brand']
class ParkingFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=Parking.Status)


class ParkingFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=Parking.Status.choices)

class Meta:
    model = Parking
    fields = ['status']

class ReservationFilter(filters.FilterSet):
    from_time = filters.DateTimeFilter(field_name="start_time", lookup_expr='gte')

    class Meta:
        model = Reservation
        fields = ['from_time']