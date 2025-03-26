from django.db import models

# Create your models here.
#Abstract Model
class Infomodel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    Change_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(Infomodel):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()

class Teacher(Infomodel):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
