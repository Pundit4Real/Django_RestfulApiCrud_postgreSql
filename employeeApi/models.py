from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=5,unique=True)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13, unique=True)