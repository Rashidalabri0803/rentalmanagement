from django.shortcuts import render, redirect
from django.core.mail import send_mail
def approve_booking(request, booking_id):
    # Retrieve the booking with the given ID
    booking = Booking.objects.get(id=booking_id)
    
    # Update the booking's is_approved field to True
    booking.is_approved = True
    booking.save()

    # Send an email to the user
    send_mail(
        'تم قبول الحجز الخاص بك للعقار',
        'تم قبول الحجز الخاص بك للعقار. نراكم قريباً!',
        'noreply@yourwebsite.com',
        [booking.user.email],
        fail_silently=False,
    )
    # Redirect the user to the booking list page
    return redirect('admin_dashboard')