from django.shortcuts import render
from .models import BlogCategory, BlogTag, Post


def all_post_view(request):
    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')
    posts = Post.objects.filter(is_active=True).order_by('-created_at')

    context = dict(
        categories=categories,
        tags=tags,
        posts=posts,
    )
    return render(request, 'blog/all_posts.html', context)