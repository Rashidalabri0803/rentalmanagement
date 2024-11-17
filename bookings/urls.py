from django.urls import path

from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('create/<int:property_id>/', views.create_booking, name='create_booking'),
    path('approve/<int:booking_id>/', views.approve_booking, name='approve_booking')
]