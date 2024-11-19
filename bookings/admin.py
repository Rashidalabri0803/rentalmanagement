from django.contrib import admin

from .models import Booking, Review


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('property', 'customer', 'start_date', 'end_date', 'status', 'cancellation_date')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('property__name', 'customer__username')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('property', 'customer', 'start_date', 'end_date', 'is_approved', 'comments')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('property', 'customer', 'rating', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('property__name', 'customer__username', 'comment')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {'fields': ('property', 'customer', 'rating', 'comment')}),
        ('Dates', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)