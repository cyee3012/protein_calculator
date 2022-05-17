from django.shortcuts import render
from .forms import ProteinForm

def home(request):
  if request.method == "POST":
    form = ProteinForm(request.POST)

    if form.is_valid():
      form.save()
      system = form.cleaned_data['system']
      weight = form.cleaned_data['weight']
      return render(request, 'calculator/results.html', {'title': 'Results', 'weight': weight})
  else:
    form = ProteinForm()

  form = ProteinForm()
  return render(request, 'calculator/home.html', {'form': form})

def about(request):
  return render(request, 'calculator/about.html', {'title': 'About'})

def results(request):
  return render(request, 'calculator/results.html', {'title': 'Results', 'weight': 'weight'})
