from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CorporateRegistrationForm

# Create your views here.

def register_corporate(request):
    if request.method == 'POST':
        form = CorporateRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = CorporateRegistrationForm()
    return render(request, 'corporate/register_corporate.html', {'form': form})
