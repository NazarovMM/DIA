from django.shortcuts import render
from django.http import HttpResponse
from .models import Team


def master(request):
    teams = Team.objects.order_by('id')
    return render(request, 'lab8/master.html', {'teams': teams})


def detail(request):
    c_id = request.GET['id']
    team = Team.objects.get(id=c_id)
    return render(request, 'lab8/detail.html', {'team': team})
