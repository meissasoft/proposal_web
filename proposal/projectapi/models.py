from django.db import models
from proposalapi.models import UserRegistration

# Create your models here.

# Project Model


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

    def __str__(self):
        return self.name


# User Project Model
class UserProject(models.Model):
    user_id = models.ForeignKey(
        UserRegistration, null=True, on_delete=models.CASCADE)
    project_id = models.ForeignKey(
        Project, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


# Project Template Model
class ProjectTemplate(models.Model):
    class Status(models.IntegerChoices):
        CREATED = 1
        DELETED = 2

    name = models.CharField(max_length=500)
    content = models.CharField(max_length=20000, default=None)
    status = models.PositiveSmallIntegerField(
        choices=Status.choices, default=Status.CREATED)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


# Proposal Template Model
class ProposalTemplate(models.Model):
    class Status(models.IntegerChoices):
        CREATED = 1
        DELETED = 2

    name = models.CharField(max_length=500)
    content = models.CharField(max_length=20000, default=None)
    status = models.PositiveSmallIntegerField(
        choices=Status.choices, default=Status.CREATED)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


# User Project Template Model
class UserProjectTemplate(models.Model):
    user_id = models.ForeignKey(
        UserRegistration, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


# User Proposal Template Model
class UserProposaltemplate(models.Model):
    user_id = models.ForeignKey(
        UserRegistration, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


# JobPost Model
class JobPost(models.Model):
    proposal_template_id = models.ForeignKey(
        ProposalTemplate, null=True, on_delete=models.CASCADE)
    project_id = models.ForeignKey(
        Project, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        UserRegistration, null=True, on_delete=models.CASCADE)
    job_url_link = models.CharField(max_length=500, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


class Attribute(models.Model):

    name = models.CharField(max_length=500, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class UserAttribute(models.Model):
    user = models.ForeignKey(
        UserRegistration, null=True, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=500, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


class ProjectAttribute(models.Model):
    project = models.ForeignKey(
        Project, null=True, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=500, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
