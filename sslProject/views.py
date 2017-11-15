from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from details.models import *

@login_required
class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            if request.user.is_authenticated():
                context={
                    'user':request.user
                }
                return render(request , "test.html" , context)
            # else:
            #     return HttpResponseRedirect('');
        return super().get(request, *args, **kwargs)

def List(request):
    users = ProfileDetails.objects.all()
    context={
        'users': users
    }
    return render(request,'list.html', context)

def ProfilePage(request, username):
    users = ProfileDetails.objects.get(username__username=username)
    return render(request, 'profile.html',{'users':users, 'username':username})

def ProfileTeachingPage(request, username):
    users = TeachingDetails.objects.filter(username__username=username)
    return render(request, 'profile_teaching.html',{'users':users, 'username':username})

def ProfilePublicationPage(request, username):
    users = PublicationDetails.objects.filter(username__username=username)
    return render(request, 'profile_publication.html',{'users':users, 'username':username})

def ProfileStudentPage(request, username):
    users = StudentsDetails.objects.filter(username__username=username)
    return render(request, 'profile_student.html',{'users':users, 'username':username})

def ProfileRecognitionPage(request, username):
    users = ProfileDetails.objects.filter(username__username=username)
    return render(request, 'profile_recognition.html',{'users':users, 'username':username})

def ProfileProjectPage(request, username):
    users = ProjectDetails.objects.filter(username__username=username)
    return render(request, 'profile_project.html',{'users':users, 'username':username})
