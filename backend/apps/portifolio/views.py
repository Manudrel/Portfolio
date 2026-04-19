from django.shortcuts import render
from .models import Project, Skill, Experience


def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()

    return render(request, 'index.html', {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
    })