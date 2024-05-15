from django.contrib import admin
from .models import User, Winner

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'age',
        'created_at',
    ]


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'medal',
        'sport',
        'score',
    ]
