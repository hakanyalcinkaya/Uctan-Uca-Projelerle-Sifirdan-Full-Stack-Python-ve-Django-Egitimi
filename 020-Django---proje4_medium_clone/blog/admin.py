from django.contrib import admin
from .models import Category, Tag, BlogPost, UserPostFav


@admin.register(UserPostFav)
class UserPostFavAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user', 
        'post',
        'is_deleted',
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title', 
        'is_active'
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title', 
        'is_active'
    ]


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title', 
        'is_active',
        'view_count',
    ]