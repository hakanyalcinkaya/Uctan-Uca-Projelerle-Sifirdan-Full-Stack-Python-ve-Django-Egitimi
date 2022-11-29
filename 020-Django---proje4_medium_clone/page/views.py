from django.shortcuts import render


def home_view(request):
    context = {}
    return render(request, 'page/home_page.html', context)