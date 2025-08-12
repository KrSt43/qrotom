from django import forms
from .models import CarAdvertisement, CarImage

class CarAdvertisementForm(forms.ModelForm):
    class Meta:
        model = CarAdvertisement
        exclude = ['seller', 'created_at', 'updated_at', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image', 'is_primary'] 