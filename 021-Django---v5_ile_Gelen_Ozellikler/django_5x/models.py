from django.db import models
from django.db.models.functions import Now
from django.db.models import F
from faker import Faker

# Link: https://docs.djangoproject.com/en/5.0/releases/5.0/


class User(models.Model):
    full_name = models.CharField(max_length=100)
    # age = models.SmallIntegerField(default=18)
    # created_at=models.DateTimeField(auto_now_add=True)
    # Django 5.x ile gelen db_default ozelligi:
    age = models.SmallIntegerField(db_default=18)
    created_at=models.DateTimeField(db_default=Now())


Medal = models.TextChoices("Medal", "GOLD SILVER BRONZE")

SPORT_CHOICES = {  # Using a mapping instead of a list of 2-tuples.
    "running": "Running",
    "Martial Arts": {"judo": "Judo", "karate": "Karate"},
    "Racket": {"badminton": "Badminton", "tennis": "Tennis"},
    "unknown": "Unknown",
}

def get_scores():
    return [(i, str(i)) for i in range(1, 11)]

def get_jobs():
    faker = Faker()
    return [(faker.job(), faker.job().upper()) for i in range(10)]


class Winner(models.Model):
    name = models.CharField(max_length=20)
    medal = models.CharField(max_length=20, choices=Medal)  # Using `.choices` not required.
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES)
    score = models.IntegerField(choices=get_scores)
    job = models.CharField(max_length=100, default="", choices=get_jobs)


# Database generated model field (VeriTabaninda Otomatik Hesaplanarak Olusturulmus Bilgiler)

class Square(models.Model):
    side = models.IntegerField()
    area = models.GeneratedField(
        expression=F("side") * F("side"),
        output_field=models.BigIntegerField(),
        db_persist=True,
    )


class ProductItem(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(db_default=1)
    total_price = models.GeneratedField(
        expression=F("price") * F("quantity"),
        output_field=models.DecimalField(max_digits=12, decimal_places=2),
        db_persist=True,
    )