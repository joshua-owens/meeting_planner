from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))
