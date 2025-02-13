from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')