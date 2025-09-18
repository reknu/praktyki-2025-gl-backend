from django.db import models
from .employee import Employee

class User(models.Model):
    password = models.CharField(max_length=255)
    account_creation_date = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_authenticated(self):
        
        return True