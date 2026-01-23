from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64)
    usn = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    collage = models.CharField(max_length=64)
    degree = models.CharField(max_length=64)
    branch = models.CharField(max_length=64)
    semester = models.IntegerField()

class Professor(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    collage = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    qualification = models.CharField(max_length=64)
