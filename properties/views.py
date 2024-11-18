from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Property, PropertyImage, PropertyCatagory
from .forms import PropertyForm, PropertyImageForm, PropertyCatagoryForm

@login_required
def property_list(request):
    properties = Property.objects.filter(available=True)
    return render(request, 'properties/property_list.html', {'properties': properties})

@login_required
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    images = property_obj.images.all()
    return render(request, 'properties/property_detail.html', {'property': property_obj, 'images': images})

@login_required
def add_property(request):
    if not request.user.is_admin:
        return redirect('unauthorized')
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.save()
            return redirect('properties:property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form})

@login_required
def add_property_image(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.property = property_obj
            image.save()
            return redirect('properties:property_detail', property_id=property_id)
    else:
        form = PropertyImageForm()
    return render(request, 'properties/add_property_image.html', {'form': form, 'property': property_obj})

@login_required
def add_category(request):
    if not request.user.is_admin:
        return redirect('users:dashboard')
    if request.method == 'POST':
        form = PropertyCatagoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('properties:property_list')
    else:
        form = PropertyCatagoryForm()
    return render(request, 'properties/add_category.html', {'form': form})