from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=False, verbose_name="عميل")
    is_admin = models.BooleanField(default=False, verbose_name="مشرف")

    def __str__(self):
        return self.username