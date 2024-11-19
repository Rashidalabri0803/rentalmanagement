from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPES = (
        ('Customer', 'عميل'),
        ('Owner', 'مالك')
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='Customer', verbose_name='نوع المستخدم')
    profile_picture = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name="الصورة الشخصية")
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="رقم الهاتف")
    address = models.CharField(max_length=100, blank=True, verbose_name="العنوان")
    is_verified = models.BooleanField(default=False, verbose_name=" تم التحقق")

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

    def is_customer(self):
        return self.user_type == 'Customer'

    def is_owner(self):
        return self.user_type == 'Owner'