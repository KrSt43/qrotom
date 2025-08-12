from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CorporateProfile

class CorporateRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=200, required=True)
    tax_no = forms.CharField(max_length=20, required=True)
    title = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'company_name', 'tax_no', 'title')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_corporate = True
        if commit:
            user.save()
            CorporateProfile.objects.create(
                user=user,
                company_name=self.cleaned_data['company_name'],
                tax_no=self.cleaned_data['tax_no'],
                title=self.cleaned_data['title']
            )
        return user 