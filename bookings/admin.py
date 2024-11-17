from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('property', 'customer', 'start_date', 'end_date', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'start_date', 'end_date')
    search_fields = ('property__name', 'cuustomer__username')
    list_editable = ('is_approved',)
    ordering = ('-created_at',)