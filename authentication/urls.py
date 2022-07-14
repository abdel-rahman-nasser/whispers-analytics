
from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.authentication.welcome,name="welcome"),
    path('login/',views.authentication.sign_in,name="login"),
    path('register/',views.authentication.sign_up,name="register"),
    path('sign_out/',views.authentication.sign_out,name="signout"),
]