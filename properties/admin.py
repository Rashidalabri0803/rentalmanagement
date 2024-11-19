from django.contrib import admin

from .models import Property, PropertyCatagory, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 2
    readonly_fields = ('image',)

admin.register(PropertyCatagory)
class PropertyCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'price_per_month', 'created_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('name', 'owner__username', 'location')
    list_editable = ('available',)
    inlines = [PropertyImageInline]
    ordering = ('created_at',)
    fieldsets = (
        (None, {'fields': ('name', 'description', 'price_per_month', 'location', 'category', 'owner', 'available')}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')
