from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Team
from .models import User


def index(request):
    response = ''
    for i, teamobj in enumerate(Team.objects.all()):
        response += "Team %i: %s <br>" % (i, teamobj)
    return HttpResponse(response)

def detail(request, teamid):
    try:
        name = Team.objects.get(id=teamid).name
        response = 'Team: %s <br>' % name
        response += 'Members: <br>'
        users = User.objects.filter(team__name=name)
        for username in users:
            response += '  * %s <br>' % username
    except ObjectDoesNotExist:
        response = 'fuck you'

    return HttpResponse(response)

