from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = dict()
    context['title'] = "Cleaning Services"
    return render(request, "basic/home.html", context)

def about(request):
    context = dict()
    context['title'] = "About"
    return render(request, "basic/about.html", context)

def services(request):
    context = dict()
    context['title'] = "Cleaning Services"
    return render(request, "basic/services.html", context)



def subscribe(request):
    return HttpResponse("Ok")

def portfolio(request):
    context = dict()
    context['title'] = "Portfolio"
    return render(request, "basic/portfolio.html", context)