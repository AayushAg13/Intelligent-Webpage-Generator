from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from sslProject import settings
from . import forms
import urllib
import json

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"

def Login_User(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req =  urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())

                if result['success']:
                    login(request, user)
                    return redirect('/test/about_me')
                else:
                    return render(request, 'users/login.html', {'error_message': 'Invalid Captcha'})
            else:
                return render(request, 'users/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'users/login.html', {'error_message': 'Invalid Login'})
    return render(request, 'users/login.html')
