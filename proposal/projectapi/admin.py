from django.contrib import admin

from .models import Project,ProjectTemplate, UserProjectTemplate

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'tags', 'project_url_link','languages','platform','project_github_link','project_earning',]



from django.contrib import admin

# Register your models here.
