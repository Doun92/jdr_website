from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

# Models import
from .models import Scénario

# Create your views here.


def index_scenarios(request):
    # return HttpResponse("Première pierre de mon site pour les jeux de rôle.")

    liste_scenarios = Scénario.objects.all
    context = {
        "liste_scenarios": liste_scenarios
        }

    return render(request, "scenario/index.html", context)


def detail_scenario(request, scenario_id):
    scenario = get_object_or_404(Scénario, pk=scenario_id)
    context = {
        "scenario": scenario
    }
    return render(request, "scenario/detail.html", context)