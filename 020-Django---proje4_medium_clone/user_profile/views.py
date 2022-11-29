from django.shortcuts import render


def login_view(request):
    # login olan kullanici direkt olaran ana sayfaya gitsin..
    context = dict()
    return render(request, 'user_profile/login.html', context)