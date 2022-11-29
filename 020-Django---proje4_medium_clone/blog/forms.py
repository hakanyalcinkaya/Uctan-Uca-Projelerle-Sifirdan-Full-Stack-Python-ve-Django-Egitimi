from django import forms
from .models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]
    
    