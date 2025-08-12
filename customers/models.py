from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    TCKN = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
