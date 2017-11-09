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
        user = ProfileDetails.objects.get(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/about_me/create')

    context={
        'user':user,
    }
    return render(request, 'about_me.html', context)

@login_required
def About_Me_Edit(request):
    instance = models.ProfileDetails.objects.get(username__username=request.user.username)
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
        user = TeachingDetails.objects.filter(username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/teaching/create')

    context={
        'user':user,
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
