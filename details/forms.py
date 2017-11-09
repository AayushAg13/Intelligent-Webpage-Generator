from details.models import *
from django.forms import ModelForm

class AboutForm(ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ("name","designation","department","institute",
        "office","email","phone")

class TeachingForm(ModelForm):
    class Meta:
        model = TeachingDetails
        fields = ("year","semester","course_name","course_description")
