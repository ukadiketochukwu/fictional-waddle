from django.contrib.auth.models import AbstractUser
from django.db import models

class LogisticUser(AbstractUser):
    ROLE_CHOICES = (
        ('load_owner', 'Load Owner'),
        ('truck_owner', 'Truck Owner'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
