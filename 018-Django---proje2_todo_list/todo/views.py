from django.shortcuts import render
from .models import Todo
# from django.http import HttpResponse
from django.http import Http404


def home_view(request):
    # todos = Todo.objects.all()
    # todos = Todo.objects.filter(is_active=True)
    # todos = todos.filter(title__icontains="todo")

    todos = Todo.objects.filter(
        is_active=True,
        # title__icontains="todo",
    )

    context = dict(
        todos=todos
    )
    return render(request, 'todo/todo_list.html', context)


def todo_detail_view(request, id):
    try:
        todo = Todo.objects.get(pk=id)
        context = dict(
            todo=todo,
        )
        return render(request, 'todo/todo_detail.html', context)
    except Todo.DoesNotExist:
        raise Http404