from django.db import models

from users.models import User

class PropertyCatagory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="اسم الفئة")
    description = models.TextField(blank=True, verbose_name="وصف الفئة")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "فئة العقار"
        verbose_name_plural = "فئات العقارات"

class PropertyFeature(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="الميزة")
    description = models.TextField(blank=True, verbose_name="وصف الميزة")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ميزة العقار"
        verbose_name_plural = "ميزات العقارات"
        
class Property(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم العقار")
    description = models.TextField(verbose_name="وصف العقار")
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر لكل شهر")
    location = models.CharField(max_length=255, verbose_name="الموقع")
    category = models.ForeignKey(PropertyCatagory, on_delete=models.SET_NULL, null=True, related_name="properties", verbose_name="الفئة")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties', verbose_name="مالك العقار")
    available = models.DateField(default=True, verbose_name="متاح للايجار")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    def __str__(self):
        return self.name

    def calculate_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum(review.rating for review in reviews) / reviews.count()
        return 0

    class Meta:
        verbose_name = "عقار"
        verbose_name_plural = "العقارات"
        ordering = ['-created_at']

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images', verbose_name="العقار")
    image = models.ImageField(upload_to='properties/', verbose_name="الصورة")
    caption = models.CharField(max_length=255, blank=True,  verbose_name="وصف الصورة")

    def __str__(self):
        return f"صورة: {self.property.name}"

    class Meta:
        verbose_name = "صورة العقار"
        verbose_name_plural = "صور العقارات"