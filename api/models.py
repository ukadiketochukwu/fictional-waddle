from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class LogisticUser(AbstractUser):
    ROLE_CHOICES = (
        ('load_owner', 'Load Owner'),
        ('truck_owner', 'Truck Owner'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class Truck(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=100)
    # add more fields as needed

    def __str__(self):
        return self.title

class Load(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.IntegerField()
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    # add more fields as needed

    def __str__(self):
        return self.description[:30]
