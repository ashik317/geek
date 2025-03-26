from symtable import Class

from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)

class Student(models.Model):
    age = models.ImageField()

class Product(models.Model):
    price = models.FloatField()

class Event(models.Model):
    event_date = models.DateField()

class Post(models.Model):
    pub_date = models.DateTimeField()

class Task(models.Model):
    is_active = models.BooleanField()

class Author (models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Courses(models.Model):
    name = models.CharField(max_length=100)

class Students(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField(Courses)

class Contact(models.Model):
    email = models.EmailField()

class UserProfile(models.Model):
    Profile_picture = models.ImageField(upload_to='profile_pics/')


Item_codes = models.CommaSeparatedIntegerField(max_length=100)

Item_codes = models.CommaSeparatedIntegerField(max_length=100)

#CommaSeparatedIntegerField
class Item(models.Model):
    Item_codes = models.CommaSeparatedIntegerField(max_length=100)

#JOINED FIELDS
class Products(models.Model):
    properties = models.JSONField()

class Order(models.Model):
    items_name = ArrayField(models.CharField(max_length=100))