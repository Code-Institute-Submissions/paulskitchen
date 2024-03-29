from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    guests = models.IntegerField(null=True)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

"""model for form"""
class Contact(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(max_length= 250)
    message = models.CharField(max_length=500)

