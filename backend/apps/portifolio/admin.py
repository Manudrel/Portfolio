from django.contrib import admin
from .models import Project, Skill, Experience, SkillCategory

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'github_link')
    search_fields = ('title', 'description')
    list_filter = ('tags',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)   

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_year')
    search_fields = ('position', 'company')
    list_filter = ('start_year',)

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

