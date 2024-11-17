from django.contrib import admin

from .models import Property

admin.site.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'price_per_month', 'location', 'available', 'created_at')
    list_filter = ('available', 'location')
    search_fields = ('name', 'location')
    list_editable = ('available',)
    ordering = ('created_at',)
