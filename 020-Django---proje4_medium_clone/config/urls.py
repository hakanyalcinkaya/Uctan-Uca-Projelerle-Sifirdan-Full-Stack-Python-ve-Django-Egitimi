"""config URL Configuration
https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from page.views import home_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('admin/', admin.site.urls),
]
