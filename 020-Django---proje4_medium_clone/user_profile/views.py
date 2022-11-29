from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    # login olan kullanici direkt olaran ana sayfaya gitsin..
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username } Daha Once Login Olmussun ;)')
        return redirect('home_view')

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
            messages.success(request, f'{request.user.username } Login Oldun')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)