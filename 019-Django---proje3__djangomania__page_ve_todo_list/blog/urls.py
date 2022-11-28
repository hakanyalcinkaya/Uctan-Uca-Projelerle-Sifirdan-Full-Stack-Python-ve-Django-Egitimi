from django.urls import path
from blog.views import all_post_view

app_name = 'blog'

urlpatterns = [
    path('', all_post_view, name='all_post_view')
]