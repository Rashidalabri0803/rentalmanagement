from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Property
from .forms import PropertyForm

@login_required
def property_list(request):
    properties = Property.objects.filter(available=True)
    return render(request, 'properties/property_list.html', {'properties': properties})

@login_required
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'properties/property_detail.html', {'property': property_obj})

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
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form}