from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomerProfile

class CustomerRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    TCKN = forms.CharField(max_length=11, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'name', 'surname', 'TCKN')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_corporate = False
        if commit:
            user.save()
            CustomerProfile.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                surname=self.cleaned_data['surname'],
                TCKN=self.cleaned_data['TCKN']
            )
        return user 