from django import forms
from django.core import validators
from tinymce.widgets import TinyMCE
from .models import BlogPost

# Our Validator:
def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("Kendi Denetimimiz.. En Az 3 Karakter Olmali..")


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 20}))
    # title = forms.CharField(validators=[validators.MinLengthValidator(3, message="Oppss.. En Az 3 Karakter Olmali..")])
    title = forms.CharField(validators=[min_length_3, ])

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]
    
    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3:
    #         raise forms.ValidationError('Ooo En Az 3 Karakter Olmali..')
    #     return title
    