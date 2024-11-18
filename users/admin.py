from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefautUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_admin', 'is_staff')
    list_filter = ('is_customer', 'is_admin', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_customer', 'is_admin', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'profile_picture')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('date_joined', 'last_login')