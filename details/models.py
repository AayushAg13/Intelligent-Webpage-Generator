from django.db import models
from django.contrib.auth.models import User

class ProfileDetails(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=128)
    institute = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

import datetime
YEAR_CHOICES = []
SEM_CHOICES = [(1, 'Odd Semester'), (2, 'Even Semester')]
for r in range(1993, (datetime.datetime.now().year+1)):
    s = str(r)+"-"+str(r+1)
    YEAR_CHOICES.append((r,s))


class TeachingDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    year=models.CharField(max_length=10, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=100, choices=SEM_CHOICES)
    course_name = models.CharField(max_length=255)
    course_description = models.CharField(max_length=255)
