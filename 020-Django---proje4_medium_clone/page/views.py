from django.shortcuts import render
from blog.models import BlogPost, Tag, Category


def home_view(request):
    posts = BlogPost.objects.filter(is_active=True) # .order_by('-created_at')
    top_posts = posts.order_by('-view_count')[:6]
    tags = Tag.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    context = dict(
        categories=categories,
        posts=posts,
        tags=tags,
        top_posts=top_posts,
    )
    return render(request, 'page/home_page.html', context)