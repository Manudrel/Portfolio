from django.shortcuts import render
from .models import Project, SkillCategory, Experience



def index(request):
    projects = Project.objects.all()
    categories= SkillCategory.objects.prefetch_related('skills').all()
    experiences = Experience.objects.all().order_by('-start_year')

    return render(request, 'index.html', {
        'projects': projects,
        'categories': categories,
        'experiences': experiences,
    })