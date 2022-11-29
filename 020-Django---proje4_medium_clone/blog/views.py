from django.shortcuts import render
from .forms import BlogPostModelForm
from .models import Category, Tag, BlogPost


def create_blog_post_view(request):
    form = BlogPostModelForm()
    context = dict(
        form=form
    )
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'blog/create_blog_post.html', context)
