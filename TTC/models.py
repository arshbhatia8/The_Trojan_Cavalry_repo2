from django.db import models

# Create your models here.
class Employer(models.Model):
    Employer_Name=models.CharField(max_length=300)
    location=models.CharField(max_length=300)
    Employer_PhNo=models.CharField(max_length=300)
    Employer_Email=models.EmailField(max_length=300)

    def __str__(self):
        return self.Employer_Name

class Employee(models.Model):
    Employee_Name=models.CharField(max_length=300)
    Employee_PhNo=models.CharField(max_length=400)

    def __str__(self):
        return self.Employee_Name