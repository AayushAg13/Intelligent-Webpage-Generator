from django.db import models
from django.contrib.auth.models import User

class ProfileDetails(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=128)
    college = models.CharField(max_length=255)
    room_no = models.CharField(max_length=255)
    joining_year = models.CharField(max_length=255)

    def __str__(self):
        return self.name
