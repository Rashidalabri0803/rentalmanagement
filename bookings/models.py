from django.db import models

from properties.models import Property
from users.models import User


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings', verbose_name="العقار")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name="العميل")
    start_date = models.DateField(verbose_name="تاريخ البدء")
    end_date = models.DateField(verbose_name="تاريخ النهاية")
    is_approved = models.BooleanField(default=False, verbose_name="مقبول")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    def __str__(self):
        return f"{self.customer.username} - {self.property.name} ({self.start_date} إلى {self.end_date})"