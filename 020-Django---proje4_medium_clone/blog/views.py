from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BlogPostModelForm
from .models import Category, Tag, BlogPost


@login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form = BlogPostModelForm()
    context = dict(
        form=form
    )
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
        
    return render(request, 'blog/create_blog_post.html', context)
