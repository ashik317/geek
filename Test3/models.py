from django.db import models
from django.db.models import Model


# Create your models here.
# OneToOne Relationship
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    locations = models.CharField(max_length=100)

#OneToMany (ManyTOOne) Relationship
class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

#MamyTOMany Relationship
class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

# Self Referential Relationship
#Category model with parent-child relationships

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

# Reversed relation (related name)
# Comment and Article models
class Article(models.Model):
    title = models.CharField(max_length=100)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

# ManyToMany Through model
#Actor, Movie, and Role model

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, through = 'Role')

class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100)
