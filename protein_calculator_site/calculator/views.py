from django.shortcuts import render, redirect
from .forms import ProteinForm

# weight = 'no weight entered'
# system = 'no system selected'

def home(request):
  form = ProteinForm()
  return render(request, 'calculator/home.html', {'form': form})

def about(request):
  return render(request, 'calculator/about.html', {'title': 'About'})

def results(request):
  if request.method == "POST":
    form = ProteinForm(request.POST)
    weight = request.POST['weight']
    system = request.POST['system']
    print(weight)
  return render(request, 'calculator/results.html', {'title': 'Results','weight': weight, 'system': system})
