from django.db import models

# Create your models here.
# Abstract Base Class
class AbstractProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    class Meta:
        abstract = True

# Multitable Product
class Book(AbstractProduct):
    author = models.CharField(max_length=100)

# Proxy Models
class DiscountedProduct(AbstractProduct):
    class Meta:
        proxy = True

    def discounted_price(self):
        return self.price * 0.9