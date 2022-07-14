from django import views
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.Scraping_Operations.home, name="home"),
    path('sections/', views.Scraping_Operations.sections, name="sections"),
    path('results/', views.Scraping_Operations.results, name="results"),
    path('home_data/', views.Scraping_Operations.home_data, name="home_data"),
]
