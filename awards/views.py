from django.shortcuts import render,redirect
from django.http.response import Http404
from .models import Project,User,Profile


# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')

def home(request):
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request, 'home.html', {"projects":projects, "users": users})

