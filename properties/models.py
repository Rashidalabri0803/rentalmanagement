from django.db import models

from users.models import User


class Property(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
        return self.name