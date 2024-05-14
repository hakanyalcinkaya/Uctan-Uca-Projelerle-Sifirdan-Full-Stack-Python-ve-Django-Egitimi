from django.db import models
from django.db.models.functions import Now


class User(models.Model):
    full_name = models.CharField(max_length=100)
    # age = models.SmallIntegerField(default=18)
    # created_at=models.DateTimeField(auto_now_add=True)
    # Django 5.x ile gelen db_default ozelligi:
    age = models.SmallIntegerField(db_default=18)
    created_at=models.DateTimeField(db_default=Now())

