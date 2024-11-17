from django.db import models

from properties.models import Property
from users.models import User


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.username} - {self.property.name}"