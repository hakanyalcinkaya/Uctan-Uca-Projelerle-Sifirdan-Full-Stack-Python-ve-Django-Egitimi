from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'todo/todo_list.html', {})

