from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from details.models import *
from details.forms import *
from django.core.exceptions import ObjectDoesNotExist

@login_required
def About_Me(request):
    user_name = request.user.username
    try:
        users = ProfileDetails.objects.get(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/about_me/create')

    context={
        'users':users,
    }
    return render(request, 'about_me.html', context)

@login_required
def About_Me_Edit(request):
    instance = ProfileDetails.objects.get(username__username=request.user.username)
    form = AboutForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/about_me')
    return render(request,'about_me_edit.html',{'form':form})

@login_required
def About_Me_Create(request):
    form = AboutForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/about_me')
    return render(request,'about_me_edit.html',{'form':form})

@login_required
def Teaching(request):
    user_name = request.user.username
    try:
        users = TeachingDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/teaching/create')

    context={
        'users':users,
    }
    return render(request, 'teaching.html', context)

@login_required
def Teaching_Edit(request):
    instance = models.TeachingDetails.objects.get(username__username=request.user.username)
    form = TeachingForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/teaching')
    return render(request,'teaching_edit.html',{'form':form})

@login_required
def Teaching_Add(request):
    form = TeachingForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/teaching')
    return render(request,'teaching_add.html',{'form':form})

@login_required
def Project(request):
    user_name = request.user.username
    try:
        users = ProjectDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/project/create')

    context={
        'users':users,
    }
    return render(request, 'project.html', context)

@login_required
def Project_Edit(request):
    instance = models.ProjectDetails.objects.get(username__username=request.user.username)
    form = ProjectForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/project')
    return render(request,'project_edit.html',{'form':form})

@login_required
def Project_Add(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/project')
    return render(request,'project_add.html',{'form':form})

@login_required
def Recognition(request):
    user_name = request.user.username
    try:
        users = RecognitionDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/recognition/create')

    context={
        'users':users,
    }
    return render(request, 'recognition.html', context)

@login_required
def Recognition_Edit(request):
    instance = models.RecognitionDetails.objects.get(username__username=request.user.username)
    form = RecognitionForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/recognition')
    return render(request,'recognition_edit.html',{'form':form})

@login_required
def Recognition_Add(request):
    form = RecognitionForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/recognition')
    return render(request,'recognition_add.html',{'form':form})

@login_required
def Publication(request):
    user_name = request.user.username
    try:
        users = PublicationDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/publication/create')

    context={
        'users':users,
    }
    return render(request, 'publication.html', context)

@login_required
def Publication_Edit(request):
    instance = models.PublicationDetails.objects.get(username__username=request.user.username)
    form = PublicationForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/publication')
    return render(request,'publication_edit.html',{'form':form})

@login_required
def Publication_Add(request):
    form = PublicationForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/publication')
    return render(request,'publication_add.html',{'form':form})

@login_required
def Students(request):
    user_name = request.user.username
    try:
        users = StudentsDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/students/create')

    context={
        'users':users,
    }
    return render(request, 'students.html', context)

@login_required
def Students_Edit(request):
    instance = models.StudentsDetails.objects.get(username__username=request.user.username)
    form = StudentsForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/students')
    return render(request,'students_edit.html',{'form':form})

@login_required
def Students_Add(request):
    form = StudentsForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/students')
    return render(request,'students_add.html',{'form':form})
