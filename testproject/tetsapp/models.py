from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    category=models.CharField(max_length=25)
