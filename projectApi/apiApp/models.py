from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    company_name=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.CharField(max_length=6)
    email=models.EmailField(unique=True,max_length=50)
    web=models.URLField(max_length=100)
    age=models.IntegerField(max_length=3)
    def __str__(self):
        return self.first_name+" "+self.last_name