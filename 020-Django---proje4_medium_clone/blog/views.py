from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.forms import BlogPostModelForm
from blog.models import Category, Tag, BlogPost


@login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form = BlogPostModelForm()
    
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("Valid Oldu..")
            f = form.save(commit=False)
            f.user = request.user
            # f.save()
    
    context = dict(
        form=form
    )
    return render(request, 'blog/create_blog_post.html', context)
