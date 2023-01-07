import email
from rest_framework import serializers
from .models import Project, ProjectTemplate, ProposalTemplate


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'tags', 'project_url_link',
                  'languages', 'platform', 'project_github_link', 'project_earning')


class ProjectTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTemplate
        fields = "__all__"


class ProposalTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalTemplate
        fields = "__all__"
