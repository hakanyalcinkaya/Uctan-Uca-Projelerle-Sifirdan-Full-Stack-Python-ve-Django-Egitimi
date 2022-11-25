from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        # 'created_at',
        # 'updated_at',
    ]

admin.site.register(Todo, TodoAdmin)