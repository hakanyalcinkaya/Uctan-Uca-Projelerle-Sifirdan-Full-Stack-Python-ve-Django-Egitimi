from django.urls import path
from .views import login_view, logout_view, register_view, profile_edit_view, user_fav_view

app_name = 'user_profile'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('favs/', user_fav_view, name='user_fav_view'),
    path('profile/edit/', profile_edit_view, name='profile_edit_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
]
