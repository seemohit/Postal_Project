from django.db import models

# Create your models here.
class Student(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    msg = models.TextField()
    dat = models.DateTimeField(auto_now_add=True)