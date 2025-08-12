from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CarAdvertisementForm, CarImageForm
from .models import CarAdvertisement, CarImage

# Create your views here.

@login_required
def create_advertisement(request):
    if request.method == 'POST':
        form = CarAdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.seller = request.user
            advertisement.save()
            images = request.FILES.getlist('image')
            for idx, image in enumerate(images):
                CarImage.objects.create(
                    car=advertisement,
                    image=image,
                    is_primary=(idx == 0)
                )
            messages.success(request, 'Advertisement created successfully!')
            return redirect('advertisement_detail', pk=advertisement.pk)
    else:
        form = CarAdvertisementForm()
    return render(request, 'advertisements/create_advertisement.html', {
        'form': form,
        'image_form': CarImageForm()
    })

def advertisement_list(request):
    advertisements = CarAdvertisement.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements})

def advertisement_detail(request, pk):
    advertisement = get_object_or_404(CarAdvertisement, pk=pk)
    images = advertisement.images.all()
    return render(request, 'advertisements/advertisement_detail.html', {
        'advertisement': advertisement,
        'images': images
    })

@login_required
def my_advertisements(request):
    advertisements = CarAdvertisement.objects.filter(seller=request.user).order_by('-created_at')
    return render(request, 'advertisements/my_advertisements.html', {'advertisements': advertisements})

@login_required
def edit_advertisement(request, pk):
    advertisement = get_object_or_404(CarAdvertisement, pk=pk, seller=request.user)
    if request.method == 'POST':
        form = CarAdvertisementForm(request.POST, instance=advertisement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Advertisement updated successfully!')
            return redirect('advertisement_detail', pk=advertisement.pk)
    else:
        form = CarAdvertisementForm(instance=advertisement)
    return render(request, 'advertisements/edit_advertisement.html', {'form': form})

@login_required
def delete_advertisement(request, pk):
    advertisement = get_object_or_404(CarAdvertisement, pk=pk, seller=request.user)
    if request.method == 'POST':
        advertisement.delete()
        messages.success(request, 'Advertisement deleted successfully!')
        return redirect('my_advertisements')
    return render(request, 'advertisements/delete_advertisement.html', {'advertisement': advertisement})
