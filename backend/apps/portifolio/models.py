from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    tags = models.ManyToManyField('Skill', blank=True, related_name='projects')

    def __str__(self):
        return self.title
    


class Skill(models.Model):

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Experience(models.Model):

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}" 
    
