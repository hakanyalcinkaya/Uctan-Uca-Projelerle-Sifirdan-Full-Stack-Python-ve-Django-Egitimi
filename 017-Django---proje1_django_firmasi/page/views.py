from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def home_view(request):
    # print("request:::", request.META)
    # print("request:::", request.HEADERS)
    # context = {"platform": f"Django Platformu Kullanildi ve randint ile donen veri:{randint(1, 100)} "}
    context = dict()
    return render(request, "page/home_page.html", context)


def about_us_view(request):
    page_title = "Hakkımızda"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ut ornare risus. Aliquam ac eleifend dolor. Suspendisse consectetur, orci at laoreet efficitur, sem tellus scelerisque neque, quis fringilla dolor erat id leo. Curabitur non malesuada nibh. In eu ultricies elit. Quisque tincidunt convallis tellus sit amet eleifend. Nullam nec justo pellentesque, laoreet purus eget, accumsan nisi."
    context = {
        "page_title": page_title,
    }
    context['hero_content'] = hero_content
    return render(request, "page/about_us.html", context)


def vision_view(request):
    page_title = "Vizyonumuz"
    context = dict(
        page_title=page_title,
    )
    return render(request, "page/vision.html", context)


def contact_us_view(request):
    page_title = "İletişim"
    hero_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ut ornare risus. Aliquam ac eleifend dolor. Suspendisse consectetur, orci at laoreet efficitur, sem tellus scelerisque neque, quis fringilla dolor erat id leo. Curabitur non malesuada nibh. In eu ultricies elit. Quisque tincidunt convallis tellus sit amet eleifend. Nullam nec justo pellentesque, laoreet purus eget, accumsan nisi."
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
    )
    return render(request, "page/contact_us.html", context)