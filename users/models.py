from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=False, verbose_name="عميل")
    is_admin = models.BooleanField(default=False, verbose_name="مشرف")
    profile_picture = models.ImageField(
        upload_to='users/', blank=True, null=True, verbose_name="الصورة الشخصية")

    def __str__(self):
        return self.username