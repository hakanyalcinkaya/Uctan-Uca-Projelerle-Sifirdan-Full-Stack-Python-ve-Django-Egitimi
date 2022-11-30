from django.urls import path
from .views import all_posts_view, post_detail_view

app_name = 'read'

urlpatterns = [
    path('<slug:user_slug>/', all_posts_view, name='all_posts_view'),
    path('<slug:user_slug>/<slug:post_slug>/', post_detail_view, name='post_detail_view'),
]
