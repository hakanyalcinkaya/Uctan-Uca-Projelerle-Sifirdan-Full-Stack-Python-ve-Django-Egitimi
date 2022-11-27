from todo.models import TodoCategory

def global_todo_categories_context(request):
    return dict(
        global_todo_categories=TodoCategory.objects.filter(is_active=True)
    )