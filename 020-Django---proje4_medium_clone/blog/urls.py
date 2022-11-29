from django.urls import path
from .views import create_blog_post_view

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_post_view, name='create_blog_post_view'),
]
