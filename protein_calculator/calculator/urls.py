from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="calculator-home"),
    path('about/', views.about, name="calculator-about"),
]
