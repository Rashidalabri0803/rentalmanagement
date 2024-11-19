from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'is_verified', 'is_active', 'date_joined')
    list_filter = ('user_type', 'is_verified', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('date_joined',)
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'profile_picture', 'phone_number', 'address')
        }),
        ('Permissions', {
            'fields': ('user_type', 'is_verified', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    readonly_fields = ('last_login', 'date_joined',)