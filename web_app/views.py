from django.shortcuts import render
#from web_app.projects.models import projects
from projects.models import projects
# Create your views here.

def home(request):
    project = projects.objects
    return render(request, 'index.html', {'projects': project})
    #project = blog.objects
    #return render(request, 'index.html', {'projects': project})

