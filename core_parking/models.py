from django.db import models

# Create your models here.

class Pracownik(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    pojazd = models.ForeignKey('Pojazd', on_delete=models.SET_NULL, null=True, blank=True)

class User(models.Model):
    haslo = models.CharField(max_length=255)
    data_konta = models.DateField(auto_now_add=True)
    pracownik = models.ForeignKey('Pracownik', on_delete=models.SET_NULL, null=True, blank=True)

class Pojazd(models.Model):
    nr_rej = models.CharField(max_length=10)
    marka = models.CharField(max_length=50)

class Parking(models.Model):
    nr_miejsca = models.CharField(max_length=10)
    pietro = models.IntegerField()
    status = models.IntegerField()
    
class Rezerwacja(models.Model):
    data_roz_rez = models.DateTimeField()
    data_zak_rez = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    miejsce = models.ForeignKey('Parking', on_delete=models.CASCADE)