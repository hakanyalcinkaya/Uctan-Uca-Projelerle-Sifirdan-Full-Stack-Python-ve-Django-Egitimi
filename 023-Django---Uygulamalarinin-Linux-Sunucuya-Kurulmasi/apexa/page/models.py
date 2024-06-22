from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='page')