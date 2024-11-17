from django.db import models

from users.models import User


class Property(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم العقار")
    description = models.TextField(verbose_name="وصف العقار")
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر لكل شهر")
    location = models.CharField(max_length=255, verbose_name="الموقع")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties', verbose_name="مالك العقار")
    available_at = models.DateField(default=True, verbose_name="متاح للايجار")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    def __str__(self):
        return self.name