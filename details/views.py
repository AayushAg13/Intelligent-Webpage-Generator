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
def Teaching_Edit(request, pk):
    instance = TeachingDetails.objects.get(pk=pk)
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
def Teaching_Delete(request, pk):
    instance = TeachingDetails.objects.get(pk=pk).delete()
    return redirect('/test/teaching')

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
def Project_Edit(request, pk):
    instance = ProjectDetails.objects.get(pk=pk)
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
def Project_Delete(request, pk):
    instance = ProjectDetails.objects.get(pk=pk).delete()
    return redirect('/test/project')

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
def Recognition_Edit(request, pk):
    instance = RecognitionDetails.objects.get(pk=pk)
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
def Recognition_Delete(request, pk):
    instance = RecognitionDetails.objects.get(pk=pk).delete()
    return redirect('/test/recognition')

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
def Publication_Edit(request, pk):
    instance = PublicationDetails.objects.get(pk=pk)
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
def Publication_Delete(request, pk):
    instance = PublicationDetails.objects.get(pk=pk).delete()
    return redirect('/test/publication')

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
def Students_Edit(request, pk):
    instance = StudentsDetails.objects.get(pk=pk)
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

@login_required
def Students_Delete(request, pk):
    instance = StudentsDetails.objects.get(pk=pk).delete()
    return redirect('/test/students')
