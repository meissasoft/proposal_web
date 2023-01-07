from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import JobPostSerializer, ProjectSerializer, ProjectTemplateSerializer, ProposalTemplateSerializer, UserProjectTemplateSerializer, UserProposalTemplateSerializer
from .models import JobPost, Project, ProjectTemplate, ProposalTemplate, UserProjectTemplate, UserProposaltemplate
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
# import base64
# from django.core.files.base import ContentFile
#
# Create your views here.

# Project CRUD
class CreateProject(CreateAPIView):
    serializer_class = ProjectSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            project = serializer.save()
            data['name'] = project.name
            data['description'] = project.description
            data['id'] = project.id

        else:
            data = serializer.errors
            print('Error', data.keys())

        return Response({"detail": data})


class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_project = Project.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "Project not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(get_project, many=True)
        return Response(serializer.data)


class GetProjectById(APIView):
    serializer_class = ProjectSerializer
    allowed_methods = ('GET',)

    def get(self, request, pk, *args, **kwargs):
        try:
            get_project = Project.objects.get(id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "Project not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(get_project)
        return Response(serializer.data)


class UpdateProject(UpdateAPIView):
    serializer_class = ProjectSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            project_obj = Project.objects.get(id=pk)
            print(project_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Project was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(
            instance=project_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProject(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_project_obj = Project.objects.get(id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Project was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(get_project_obj)
        get_project_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# Project Template CRUD
class CreateProjectTemplate(CreateAPIView):
    serializer_class = ProjectTemplateSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        serializer = ProjectTemplateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            projecttemplate = serializer.save()
            data['name'] = projecttemplate.name
            data['content'] = projecttemplate.content
            data['status'] = projecttemplate.status

            data['id'] = projecttemplate.id

        else:
            data = serializer.errors
            print('Error', data.keys())
        return Response({"detail": data})


class ProjectTemplateListView(ListAPIView):
    serializer_class = ProjectTemplateSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_projectTemplate = ProjectTemplate.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "Project Templates not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectTemplateSerializer(get_projectTemplate, many=True)
        return Response(serializer.data)


class UpdateProjectTemplate(UpdateAPIView):
    serializer_class = ProjectTemplateSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            projectTemplate_obj = ProjectTemplate.objects.get(id=pk)
            print(projectTemplate_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Project Template was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectTemplateSerializer(
            instance=projectTemplate_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProjectTemplate(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_projectTemplate_obj = ProjectTemplate.objects.get(id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Project Template was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectTemplateSerializer(get_projectTemplate_obj)
        get_projectTemplate_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# Proposal Template CRUD
class CreateProposalTemplate(CreateAPIView):
    serializer_class = ProposalTemplateSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        serializer = ProposalTemplateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            proposalTemplate = serializer.save()
            data['name'] = proposalTemplate.name
            data['content'] = proposalTemplate.content
            data['status'] = proposalTemplate.status
            data['id'] = proposalTemplate.id
        else:
            data = serializer.errors
            print('Error', data.keys())
        return Response({"detail": data})


class ProposalTemplateListView(ListAPIView):
    serializer_class = ProposalTemplateSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_proposalTemplate = ProposalTemplate.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "Proposal Templates not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProposalTemplateSerializer(
            get_proposalTemplate, many=True)
        return Response(serializer.data)


class UpdateProposalTemplate(UpdateAPIView):
    serializer_class = ProposalTemplateSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            proposalTemplate_obj = ProposalTemplate.objects.get(id=pk)
            print(proposalTemplate_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Proposal Template was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProposalTemplateSerializer(
            instance=proposalTemplate_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProposalTemplate(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_proposalTemplate_obj = ProposalTemplate.objects.get(id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Proposal Template was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProposalTemplateSerializer(get_proposalTemplate_obj)
        get_proposalTemplate_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# User Project Template CRUD
class CreateUserProjectTemplate(CreateAPIView):
    serializer_class = UserProjectTemplateSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        user_id = request.user.id
        serializer = UserProjectTemplateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['user_id'] = user_id

        else:
            data = serializer.errors
            print('Error', data.keys())
        return Response({"detail": data})


class UserProjectTemplateListView(ListAPIView):
    serializer_class = UserProjectTemplateSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_userprojectTemplate = UserProjectTemplate.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "User Project Templates not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProjectTemplateSerializer(
            get_userprojectTemplate, many=True)
        return Response(serializer.data)


class UpdateUserProjectTemplate(UpdateAPIView):
    serializer_class = UserProjectTemplateSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            userprojectTemplate_obj = UserProjectTemplate.objects.get(id=pk)
            print(userprojectTemplate_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This User Project Template was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProjectTemplateSerializer(
            instance=userprojectTemplate_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserProjectTemplate(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_userprojectTemplate_obj = UserProjectTemplate.objects.get(
                id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This User Project Template was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProjectTemplateSerializer(get_userprojectTemplate_obj)
        get_userprojectTemplate_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# User Proposal Template CRUD
class CreateUserProposalTemplate(CreateAPIView):
    serializer_class = UserProposalTemplateSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        user_id = request.user.id
        serializer = UserProposalTemplateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['user_id'] = user_id
        else:
            data = serializer.errors
            print('Error', data.keys())
        return Response({"detail": data})


class UserProposalTemplateListView(ListAPIView):
    serializer_class = UserProposalTemplateSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_userproposalTemplate = UserProposaltemplate.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "User Proposal Templates not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProposalTemplateSerializer(
            get_userproposalTemplate, many=True)
        return Response(serializer.data)


class UpdateUserProposalTemplate(UpdateAPIView):
    serializer_class = UserProposalTemplateSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            userproposalTemplate_obj = UserProposaltemplate.objects.get(id=pk)
            print(userproposalTemplate_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This User Proposal Template was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProposalTemplateSerializer(
            instance=userproposalTemplate_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserProposalTemplate(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_userproposalTemplate_obj = UserProposaltemplate.objects.get(
                id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This User Proposal Template was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserProposalTemplateSerializer(
            get_userproposalTemplate_obj)
        get_userproposalTemplate_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


# JobPost CRUD
class CreateJobPost(CreateAPIView):
    serializer_class = JobPostSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        serializer = JobPostSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            JobPostTemplate = serializer.save()
            data['proposal_template_id'] = JobPostTemplate.proposal_template_id
            data['project_id'] = JobPostTemplate.project_id
            data['user_id'] = JobPostTemplate.user_id
            data['job_url_link'] = JobPostTemplate.job_url_link
        else:
            data = serializer.errors
            print('Error', data.keys())
        return Response({"detail": data})


class JobPostListView(ListAPIView):
    serializer_class = JobPostSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_JobPost = JobPost.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "JobPost not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = JobPostSerializer(
            get_JobPost, many=True)
        return Response(serializer.data)


class UpdateJobPost(UpdateAPIView):
    serializer_class = JobPostSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            JobPost_obj = JobPost.objects.get(id=pk)
            print(JobPost_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This JobPost was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = JobPostSerializer(
            instance=JobPost_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteJobPost(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_JobPost_obj = JobPost.objects.get(
                id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This JobPost was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = JobPostSerializer(
            get_JobPost_obj)
        get_JobPost_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
