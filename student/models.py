from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=25, null=False)
    Subject = models.ForeignKey(Courses, on_delete=models.CASCADE, null=False)
