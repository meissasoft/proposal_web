import email
from rest_framework import serializers
from .models import Project, ProjectTemplate


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','description','tags','project_url_link','languages','platform','project_github_link','project_earning',
                  )

class ProjectTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTemplate
        fields = "__all__"




