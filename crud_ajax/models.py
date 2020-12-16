from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    roll_no = models.CharField(max_length=100, blank=True)
    class_name = models.CharField(max_length=100, blank=True)