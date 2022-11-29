from django.shortcuts import render
from .forms import PostModelForm
from .models import Category, Tag, Post


def create_blog_post_view(request):
    form = PostModelForm()
    context = dict(
        form=form
    )
    return render(request, 'blog/create_blog_post.html', context)
