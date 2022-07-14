from django import views
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.social_media_monitoring_index,
        name="social_media_monitoring_index"
    ),
    path(
        'facebook_data',
        views.social_media_monitoring_facebook_data,
        name="social_media_monitoring_facebook_data"
    ),
    path(
        'instagram_data',
        views.social_media_monitoring_instagram_data,
        name="social_media_monitoring_instagram_data"
    ),
    path(
        'twitter_data',
        views.social_media_monitoring_twitter_data,
        name="social_media_monitoring_twitter_data"
    ),
    path(
        'user_details',
        views.social_media_monitoring_user_details,
        name="social_media_monitoring_user_details"
    ),
]
