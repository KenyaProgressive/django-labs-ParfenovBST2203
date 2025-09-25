from django.shortcuts import render
from django import template
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse(u"Привет, Мир!")
    return render(request, 'templates/static_handler.html')