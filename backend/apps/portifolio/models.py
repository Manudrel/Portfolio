from django.db import models

class SkillCategory(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory, 
        on_delete=models.SET_NULL, 
        related_name='skills',
        null=True,
        blank=True
        )
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    description_pt = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    tags = models.ManyToManyField(Skill, blank=True, related_name='projects')

    def __str__(self):
        return self.title
    


class Experience(models.Model):

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_year = models.IntegerField()
    description = models.TextField()
    position_pt = models.CharField(max_length=200, blank=True)
    description_pt = models.TextField(blank=True)
    tags = models.ManyToManyField(Skill, blank=True, related_name='experiences')


    def __str__(self):
        return f"{self.position} at {self.company}" 
    
