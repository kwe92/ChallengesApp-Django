from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# URL's Uniform Resource Locator (Routes)
# - As a developer you have to plan out what URL you want to support
# - how pages will be routed from page to page based on variaous conditions
# - Mapping actions the user takes to navigate to a diffrent URL's with the propper results

# Create your views here.

# Views (request) => HttpResponse
#   - a stand alone function that represents the view for that URL

# Dynamic View (request, variable_name) => HttpResponse
# A callback that expects two arguements request && month | where month is the variable name expected in urls.py <month>


def monthlyChallengesInt(request, month):
    if month > 0 and month < 13:
        content = _returnVal(month)
        return HttpResponse(content)
    return HttpResponseNotFound(f'Must be a number between 1 and 12 inclusive. Number recieved: {month}')


def monthlyChallenges(request, month):
    content = _returnVal(month)
    if len(content.strip()) > 0:
        return HttpResponse(content)
    return HttpResponseNotFound(f'Could not find a page matching {month}')

# A function that acts as a Switch statement
# Takes in a String month which represents a key of a dictionary and checks the dictionary for said key and if the key exists its value is returned else a default value is returned


def _returnVal(month):

    switcher = {'january': 'Erroneous in our ways, we fall; But to fall implies the capability to arise; So like the pheonix you are reborn; And a new accidental form is taken; You are the same, yet different.',
                'february': 'BEGIN, begining is half the work; let half still remain, again begin this and though wilt have finished.', 'march': 'The universe and I are ONE.', 'april': 'Do not respect the judgement of any man, but hear any man small or great; but do not fear any man, for the judgement of man is gods.', 'may': 'Attention goes where awareness flows.', 'june': 'Emptiness is calmness, calmness is emptiness.', 'july': 'Anything you put your hand to, do with thy might.', 'august': 'Men who have swords and keep them sheathed will inherit the earth.', 'september': 'Ask, and ye shall receive; Seek, and ye may find; Knock, and the door shall be opened; For whoever asketh receivith, whoever seeketh findeth, whoever knocketh the door shall be opened unto him.', 'october': 'The Symbiotic Being: The Thinker && The Prover', 'november': 'If you want to be a writer, wtire.', 'december': "The man who thinks he can and the man who thinks he can't are both right, who are you?", }

    optionValues = list(switcher.values())

    if isinstance(month, str):
        return switcher.get(month, '')
    else:
        return optionValues[month]
