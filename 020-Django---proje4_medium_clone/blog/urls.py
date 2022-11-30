from django.urls import path
from blog.views import create_blog_post_view, category_view, tag_view

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_post_view, name='create_blog_post_view'),
    path('category/<slug:category_slug>/', category_view, name='category_view'),
    path('tag/<slug:tag_slug>/', tag_view, name='tag_view'),
]
