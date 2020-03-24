from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return render(request, 'website/welcome.html')


def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))


def about(request):
    return HttpResponse("I'm Josh and I'm learning django")
