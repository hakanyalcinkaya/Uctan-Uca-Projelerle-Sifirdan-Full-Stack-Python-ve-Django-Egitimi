from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.forms import BlogPostModelForm
from blog.models import Category, Tag, BlogPost
import json

@login_required(login_url='user:login_view')
def create_blog_post_view(request):
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
                tag_item, created = Tag.objects.get_or_create(title=item.get('value'))
                f.tag.add(tag_item)
    
    context = dict(
        form=form
    )
    return render(request, 'blog/create_blog_post.html', context)
