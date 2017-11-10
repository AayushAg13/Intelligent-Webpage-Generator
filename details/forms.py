from details.models import *
from django.forms import ModelForm
from django import forms

class AboutForm(ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ("name","designation","department","institute",
        "office","email","phone", "date_of_birth")
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'class': 'hasDatepicker'}),
        }

class TeachingForm(ModelForm):
    class Meta:
        model = TeachingDetails
        fields = ("year","semester","course_name","course_description")

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectDetails
        fields = ("project_title", "project_description","pi","co_pi","funding_agency", "start_year", "end_year")

class RecognitionForm(ModelForm):
    class Meta:
        model = RecognitionDetails
        fields = ("heading", "description")

class PublicationForm(ModelForm):
    class Meta:
        model = PublicationDetails
        fields = ("Authors", "title","journal","journal_volume","page_no", "publish_date")

class StudentsForm(ModelForm):
    class Meta:
        model = StudentsDetails
        fields = ("student_status", "degree","student_name","thesis_title","supervisor")
