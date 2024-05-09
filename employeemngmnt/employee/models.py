from django.db import models

# Create your models here.


class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.dep_name

class Employee(models.Model):
    name=models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email=models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name