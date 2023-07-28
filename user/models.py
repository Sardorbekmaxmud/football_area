from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','admin'),
        ('o','owner'),
        ('u','user'),
    )

    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)