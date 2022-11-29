from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username } Daha Once Login Olmussun ;)')
        return redirect('home_view')

    context = dict()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if len(username) < 6 or len(password) < 6:
            messages.warning(request, f'Lutfen Kullani Adi ve Sifreyi Dogru Giriniz.. 6 Karakterden Kucuk Olmamali..')
            return redirect('user_profile:login_view')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username } Login Oldun')
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)


def logout_view(request):
    messages.info(request, f'{request.user.username } Oturumun Kapatildi')
    logout(request)
    return redirect('home_view')