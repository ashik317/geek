from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def get_available_products(self):
        return self.filter(stock__get = 0)

    def get_expensive_products(self):
        return self.filter(stock__get = 100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    objects = ProductManager()