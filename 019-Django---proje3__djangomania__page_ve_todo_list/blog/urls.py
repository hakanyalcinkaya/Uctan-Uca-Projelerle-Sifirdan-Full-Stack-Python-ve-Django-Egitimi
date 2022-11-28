from django.urls import path
from blog.views import all_post_view, category_view

app_name = 'blog'

urlpatterns = [
    path('', all_post_view, name='all_post_view'),
    path('category/<slug:category_slug>/', category_view, name='category_view'),
]