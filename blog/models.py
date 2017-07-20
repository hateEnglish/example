from django.db import models


# Create your models here.

class Student(models.Model):

    id = models.IntegerField(name='stu_id', primary_key=True, auto_created=True)
    name = models.CharField(name='stu_name', max_length=50)


class Teacher(models.Model):
    id = models.IntegerField(name="tea_id", primary_key=True, auto_created=True)
    name = models.CharField(name='tea_name', max_length=50)
