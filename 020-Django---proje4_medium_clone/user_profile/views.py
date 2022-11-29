from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    # login olan kullanici direkt olaran ana sayfaya gitsin..
    context = dict()
    if request.method == "POST":
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # Bu bilgileri dogru aldik mi?
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # login oldugunu kullaniciya belli edelim!
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)