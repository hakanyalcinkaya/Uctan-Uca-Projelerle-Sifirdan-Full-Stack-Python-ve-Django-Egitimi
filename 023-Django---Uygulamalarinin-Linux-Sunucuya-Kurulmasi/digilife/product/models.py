from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')