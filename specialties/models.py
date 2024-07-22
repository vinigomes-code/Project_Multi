from django.db import models

# Create your models here.

class Specialties(models.Model):
    specialtie = models.CharField(max_length=50)
    priceNormal = models.CharField(max_length=50)
    priceCard = models.CharField(max_length=50)

    def __str__(self):
        return self.specialtie

class Exam(models.Model):
    exam = models.CharField(max_length=50)
    priceNormal = models.CharField(max_length=50)
    priceCard = models.CharField(max_length=50)

    def __str__(self):
        return self.exam