import email
from rest_framework import serializers
from .models import JobPost, Project, ProjectTemplate, ProposalTemplate, UserProjectTemplate, UserProposaltemplate


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


class UserProjectTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProjectTemplate
        fields = "__all__"


class UserProposalTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProposaltemplate
        fields = "__all__"


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = "__all__"


class CreateProposalTemplateSerializer(serializers.ModelSerializer):
    userID = serializers.IntegerField()
    projectIds = serializers.CharField()
    proposal_tempalte_id =  serializers.IntegerField()
    project_template_id = serializers.IntegerField()
    class Meta:
        model = JobPost
        fields = ["userID","projectIds","proposal_tempalte_id","project_template_id"]