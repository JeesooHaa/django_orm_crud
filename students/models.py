from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=5, default="") 
    email = models.CharField(max_length=50, default="")
    birthday = models.DateField(max_length=10)  
    age = models.IntegerField()
