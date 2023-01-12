from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=35)
    group = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()

class Professor(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=35)
    email = models.EmailField()
    profession = models.CharField(max_length=30)
    

