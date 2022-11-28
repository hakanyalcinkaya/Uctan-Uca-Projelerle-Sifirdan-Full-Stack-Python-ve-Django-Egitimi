from django.shortcuts import render, get_object_or_404
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


def category_view(request, category_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')
    posts = Post.objects.filter(
        category=category,
        is_active=True,
    ).order_by('-created_at')

    context = dict(
        category=category,
        categories=categories,
        tags=tags,
        posts=posts,
    )
    return render(request, 'blog/all_posts.html', context)


def tag_view(request, tag_slug):
    tag = get_object_or_404(BlogTag, slug=tag_slug)
    categories = BlogCategory.objects.filter(is_active=True).order_by('title')
    tags = BlogTag.objects.filter(is_active=True).order_by('title')
    posts = Post.objects.filter(
        tag=tag,
        is_active=True,
    ).order_by('-created_at')

    context = dict(
        tag=tag,
        categories=categories,
        tags=tags,
        posts=posts,
    )
    return render(request, 'blog/all_posts.html', context)