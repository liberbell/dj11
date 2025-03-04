from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
