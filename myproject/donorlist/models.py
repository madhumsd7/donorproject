from django.db import models

# Create your models here.

class donorlist(models.Model):
    BLOOD_CHOICES = (
           ('A+','A+'),
           ('A-','A-'),
           ('B+','B+'),
           ('B-','B-'),
    )
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)
    blood = models.CharField(max_length=10, choices=BLOOD_CHOICES)
    mobile_number = models.CharField(max_length = 30)
    place = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
