from django.shortcuts import render
from django.http import  HttpResponse

def home(request):
  return HttpResponse("<h1>Calculator Homepage</h1>")

def about(request):
  return HttpResponse("<h1>About</h1>"
    "<h2>What is Protein calculator?</h2>"
    "<h3>Protein calculator was created to easily calculate protein intake, to help those who are trying to gain muscle 💪🏼</h3>"
    "<p>Site created with Django and Python 🐍"
  )
