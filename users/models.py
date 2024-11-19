from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=False, verbose_name="عميل")
    is_admin = models.BooleanField(default=False, verbose_name="مشرف")
    profile_picture = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name="الصورة الشخصية")
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="رقم الهاتف")
    address = models.CharField(max_length=100, blank=True, verbose_name="العنوان")

    def __str__(self):
        return self.username

    def is_admin_user(self):
        return self.is_admin