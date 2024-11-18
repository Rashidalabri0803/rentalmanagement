from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm, ReviewForm
from .models import Booking, Review


@login_required
def booking_list(request):
    if request.user.is_admin:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(customer=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def create_booking(request, property_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.property_id = property_id
            booking.customer = request.user
            booking.save()
            return redirect('bookings:booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})

@login_required
def approve_booking(request, booking_id):
    if not request.user.is_admin:
        return redirect('unauthorized')
    booking = get_object_or_404(Booking, id=booking_id)
    booking.is_approved = True
    booking.save()
    return redirect('booking_list')

@login_required
def review_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user
            review.property = property_obj
            review.save()
            return redirect('properties:property_detail', property_id=property_id)
    else:
        form = ReviewForm()
    return render(request, 'properties/review_property.html', {'form': form, 'property': property_obj})