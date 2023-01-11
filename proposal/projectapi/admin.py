from django.contrib import admin

from .models import Attribute, Project, ProjectAttribute, UserAttribute, UserProject, ProjectTemplate, ProposalTemplate, UserProjectTemplate, UserProposaltemplate, JobPost


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'tags', 'project_url_link', 'languages',
                    'platform', 'project_github_link', 'project_earning', 'created']


@admin.register(UserProject)
class UserProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'project_id', 'created']


@admin.register(ProjectTemplate)
class ProjectTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'status', 'created']


@admin.register(ProposalTemplate)
class ProposalTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'status', 'created']


@admin.register(UserProjectTemplate)
class UserProjectTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'created']


@admin.register(UserProposaltemplate)
class UserProposaltemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'created']


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'proposal_template_id', 'project_id',
                    'user_id', 'job_url_link', 'created']


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created']


@admin.register(UserAttribute)
class UserAttributeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'attribute_value', 'created']


@admin.register(ProjectAttribute)
class ProjectAttributeAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'attribute_value', 'created']
