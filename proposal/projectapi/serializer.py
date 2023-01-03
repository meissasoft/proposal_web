import email
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','description','tags','project_url_link','languages','platform','project_github_link','project_earning',
                  )


# class TodoPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = 'title', 'description'

