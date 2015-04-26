from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import Team
from .models import User


def index(request):
    teams_list = Team.objects.all()
    context = { 'teams_list': teams_list }
    return render(request, 'teams/index.html', context)

def detail(request, teamid):
    team = get_object_or_404(Team, id=teamid)
    context = {
        'teamname' : team.name,
        'member_list' : User.objects.filter(team__name=team.name)
    }
    return render(request, 'teams/detail.html', context)

