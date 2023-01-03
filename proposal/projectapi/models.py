from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=10000, default=None)
    tags = models.CharField(max_length=1000, default=None)
    project_url_link = models.CharField(max_length=500, default=None)
    languages = models.CharField(max_length=500, default=None)
    platform = models.CharField(max_length=500, default=None)
    project_github_link = models.CharField(max_length=500, default=None)
    project_earning = models.CharField(max_length=500, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)



