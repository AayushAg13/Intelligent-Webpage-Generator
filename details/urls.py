from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'details'

urlpatterns = [
    url(r"^about_me/$", views.About_Me,name='about_me'),
    url(r"^about_me/edit$", views.About_Me_Edit,name='about_me_edit'),
    url(r"^about_me/create$", views.About_Me_Create, name='about_me_create'),
    url(r"^teaching/$", views.Teaching,name='about_me'),
    url(r"^teaching/edit$", views.Teaching_Edit,name='about_me_edit'),
    url(r"^teaching/add$", views.Teaching_Add, name='about_me_add'),
]
