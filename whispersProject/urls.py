from lib2to3.pgen2.token import NAME
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from scrape import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('home/', include('scrape.urls')),
    path('chat_bot/', include('chat_bot_b.urls')),
    path('social_media_monitoring/', include('social_media_monitoring.urls')),
    path('trends/', include('g_trends.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
