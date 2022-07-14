from django import views
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('g_trends/', views.get_g_trends, name="g_trends"),
    path('g_trends/search/', views.g_trends_search,name="g_trends_search"),
    path('bar-chart/<str:query>', views.bar_chart, name='bar-chart'),
    path('time_series/<str:query>', views.time_series, name='time_series'),
]
