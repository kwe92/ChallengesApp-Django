from django.shortcuts import render
from django.http import HttpResponse

# URL's Uniform Resource Locator (Routes)
# - As a developer you have to plan out what URL you want to support
# - how pages will be routed from page to page based on variaous conditions
# - Mapping actions the user takes to navigate to a diffrent URL's with the propper results

# Create your views here.

# Views
#   - a stand alone function that represents the view for that URL


def january(request):
    return HttpResponse('This Works!')


def february(request):
    content = 'Begin, begining is half the work; let half still remain, again begin this and though wilt have finished.'
    return HttpResponse(content)

# A callback that expects two arguements request && month | where month is the arbitrary name expected in urls.py <month>


def monthlyChallenges(request, month):
    content = _returnVal(month)
    return HttpResponse(content)

# A function that acts as a Switch statement
# Takes in a String month which represents a key of a dictionary and checks the dictionary for said key and if the key exists its value is returned else de


def _returnVal(month):
    switcher = {'january': 'This Works!',
                'february': 'BEGIN, begining is half the work; let half still remain, again begin this and though wilt have finished.'}
    return switcher.get(month, '')
