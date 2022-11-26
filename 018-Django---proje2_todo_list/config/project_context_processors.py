from todo.models import Category


def global_category_context(request):
    # global_categories=Category.objects.all()
    return dict(
        global_categories=Category.objects.filter(is_active=True)
    )
