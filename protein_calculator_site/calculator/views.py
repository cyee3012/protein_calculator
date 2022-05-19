from django.shortcuts import render, redirect
from .forms import ProteinForm

def home(request):
  form = ProteinForm()
  return render(request, 'calculator/home.html', {'form': form})

def about(request):
  return render(request, 'calculator/about.html', {'title': 'About'})

def results(request):
  if request.method == "POST":
    form = ProteinForm(request.POST)
    weight = int(request.POST['weight'])
    system = request.POST['system']
    metric_protein_grams = str(round(weight * 1.2)) + "-" + str(round(weight * 1.7))
    imperial_protein_grams = str(round(weight * 0.5)) + "-" + str(round(weight * 0.8))

    return render(request, 'calculator/results.html', {'title': 'Results','weight': weight, 'system': system, 'metric_protein_grams': metric_protein_grams, 'imperial_protein_grams': imperial_protein_grams})
