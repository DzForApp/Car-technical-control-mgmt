from django.db import models

# Create your models here.
class person(models.Model):
    national_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    Date_Naiss = models.DateField
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.TextField

    def __str__(self):
        return self.name

class car(models.Model):
    mat = models.CharField(max_length=200)
    car_mark = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    car_color = models.CharField(max_length=200)
    owner = models.ForeignKey(person, on_delete=models.CASCADE, default='0')

    def __str__(self):
        return self.mat





