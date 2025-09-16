from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from .employee import Employee

class User(models.Model):
    password = models.CharField(max_length=255)
    account_creation_date = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.full_name