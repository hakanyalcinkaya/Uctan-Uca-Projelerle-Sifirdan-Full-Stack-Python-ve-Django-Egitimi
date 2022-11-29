from django.urls import path
from .views import login_view, logout_view

app_name = 'user_profile'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]
