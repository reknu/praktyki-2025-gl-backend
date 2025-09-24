from django.db import models

class Admin(models.Model):
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=10)
