from django.contrib import admin
from .models import User, Winner, Square, ProductItem

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'age',
        'created_at',
    ]


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'medal',
        'sport',
        'score',
    ]


@admin.register(Square)
class SquareAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'side',
        'area',
    ]


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'quantity',
        'total_price',
    ]