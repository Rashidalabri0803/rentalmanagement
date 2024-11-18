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

    class Meta:
        verbose_name = "حجز"
        verbose_name_plural = "الحجوزات"
        ordering = ['-created_at']

class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews', verbose_name="العقار")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name="العميل")
    rating = models.IntegerField(verbose_name="التقييم")
    comment = models.TextField(verbose_name="التعليق")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التقييم")

    def __str__(self):
        return f"{self.customer.username} - {self.property.name} ({self.rating}/5)"

    class Meta:
        verbose_name = "تقييم"
        verbose_name_plural = "التقييمات"
        ordering = ['-created_at']