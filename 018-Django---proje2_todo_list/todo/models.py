from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Third Party Apps:
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'category_view',
            kwargs={
                "category_slug": self.slug
            }
        )


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'tag_view',
            kwargs={
                "tag_slug": self.slug
            }
        )


class Todo(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE) # BUNU kullanmayacagim cunku CASCADE yapinca 
    # Category silinirse tum TODOlar silinir..
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'todo_detail_view',
            kwargs={
                "category_slug": self.category.slug,
                "id": self.pk,
            }
        )