from django.shortcuts import render
from django.http import HttpResponse
import random 
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def blog(request):
    return render(request, 'portfolio/blog.html')
    

def about(request):    
    return render(request, 'portfolio/about.html')