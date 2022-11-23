from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # print("request:::", request.META)
    # print("request:::", request.HEADERS)
    return HttpResponse('Ana Sayfaya Hosgeldiniz..')
