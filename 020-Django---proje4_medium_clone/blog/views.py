from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import json

from blog.forms import BlogPostModelForm
from blog.models import Category, Tag, BlogPost


@login_required(login_url='user:login_view')
def fav_update_view(request):
    if request.method == 'POST':
        print(request.POST)
    return JsonResponse({"status": "OK"})


@login_required(login_url='user:login_view')
def create_blog_post_view(request):
    title = "Yeni Blog Post :"
    form = BlogPostModelForm()
    
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            print(form.cleaned_data)
            f.user = request.user
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title=item.get('value').lower())
                tag_item.is_active = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request, "Blog Postunuz Basariyla Kaydedildi..")
            return redirect('home_view')
    
    context = dict(
        form=form,
        title=title,
    )
    return render(request, 'common_components/form.html', context)


def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = BlogPost.objects.filter(tag=tag)
    context = dict(
        tag=tag,
    )
    return render(request, 'blog/post_list.html', context)


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    context = dict(
        category=category,
    )
    return render(request, 'blog/post_list.html', context)