from django.db import models
from django.contrib.auth.models import User

class CarAdvertisement(models.Model):
    FUEL_CHOICES = [
        ('Benzin', 'Benzin'),
        ('Dizel', 'Dizel'),
        ('LPG', 'LPG'),
        ('Elektrik', 'Elektrik'),
        ('Hibrit', 'Hibrit'),
    ]

    TRANSMISSION_CHOICES = [
        ('Manuel', 'Manuel'),
        ('Otomatik', 'Otomatik'),
        ('Yarı Otomatik', 'Yarı Otomatik'),
    ]

    BRAND_CHOICES = [
        ('BMW', 'BMW'),
        ('AUDI', 'AUDI'),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    kilometer = models.IntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    engine_power = models.IntegerField(help_text="HP")
    engine_size = models.FloatField(help_text="cc")
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.year}"

class CarImage(models.Model):
    car = models.ForeignKey(CarAdvertisement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.car}"
