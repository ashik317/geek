from django.db import models

# Create your models here.
#Model Method
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_length=8, decimal_places=2)
    stock = models.IntegerField()
def calculate_total_value(self):
    return self.price * self.stock
def is_in_stock(self):
    return self.stock > 0

