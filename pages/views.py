from django.shortcuts import render
from django.http import HttpResponse
from biens.models import Bien
from agents.models import Agent

def index(request):
    biens = Bien.objects.order_by('-ajout_date').filter(est_disponible=True)[:3]
    context = {
        'biens': biens,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    agents = Agent.objects.order_by('-ajout_date')
    mvp_agents = Agent.objects.all().filter(is_mvp=True)

    context = {
        'agents': agents,
        'mvp_agents': mvp_agents
    }

    return render(request, 'pages/about.html', context)



def handler404(request, exception):
    return render(request, 'pages/404.html')
