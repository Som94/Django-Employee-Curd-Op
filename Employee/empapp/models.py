from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=200)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=300)
    
