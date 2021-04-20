from django.shortcuts import render
from django.http import HttpResponse
from newsSite.template import latestNews


def index(request):
    context_dict = {'boldmessage': 'This just in...'}
    return render(request, latestNews.index.html, context=context_dict)


def stories(request):
    return
