from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Todo(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE) # BUNU kullanmayacagim cunku CASCADE yapinca 
    # Category silinirse tum TODOlar silinir..
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title