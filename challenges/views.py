from django.shortcuts import render
from django.http import HttpResponse

# URL's Uniform Resource Locator (Routes)
# - As a developer you have to plan out what URL you want to support
# - how pages will be routed from page to page based on variaous conditions
# - Mapping actions the user takes to navigate to a diffrent URL's with the propper results-

# Create your views here.


def index(request):
    return HttpResponse('This Works!')