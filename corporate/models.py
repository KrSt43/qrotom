from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CorporateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    tax_no = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
