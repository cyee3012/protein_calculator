from django.shortcuts import render

def home(request):
  return render(request, 'calculator/home.html')

def about(request):
  return render(request, 'calculator/about.html', {'title': 'About'})
