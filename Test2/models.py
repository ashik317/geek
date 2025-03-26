from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.ImageField(null=True)

class Article(models.Model):
    title = models.CharField(max_length=100, blank=True)

class Order(models.Model):
    order_number = models.CharField(max_length=100, default="0000")

GENDER_CHOICES = [
        ('a', 'male'),
        ('b', 'female'),
        ('c', 'child'),
        ('d', 'other')
    ]
class Persons(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GERNDER_CHOICES)
    username = models.CharField(max_length=100, db_index=True)
    text_name = models.CharField(max_length=100, editable=False)
class UserProfile(models.Model):
    user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)

class Product(models.Model):
    product_code = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=100)

class Car(models.Model):
    make = models.CharField(max_length=100, verbose_name="Make car")

class Employee(models.Model):
    name = models.CharField(max_length=100, help_text="Name of employee")

class Score(models.Model):
    score = models.IntegerField(MaxValueValidator(100), MinValueValidator(0))

class UserProfiles(models.Model):
    img = models.ImageField(upload_to="images/user_profile.png")

