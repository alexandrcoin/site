from django.shortcuts import render
from django.http import HttpResponse
from .models import Team


def index(request):
    response = ''
    for i, teamobj in enumerate(Team.objects.all()):
        response += "Team %i: %s <br>" % (i, teamobj)
    return HttpResponse(response)
