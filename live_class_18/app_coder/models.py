from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    email = models.EmailField()


class Student(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)
    

class Professor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)


class homeworks(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()


# Create your models here.
