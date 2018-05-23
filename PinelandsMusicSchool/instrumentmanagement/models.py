from django.db import models

# Create your models here.
class Instrument(models.Model):
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quality = models.CharField(max_length=100)
    available = models.CharField(max_length=100)
    rentalPrice = models.CharField(max_length=100)
    salePrice = models.CharField(max_length=100)