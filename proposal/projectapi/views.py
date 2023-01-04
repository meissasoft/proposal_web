from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProjectSerializer, ProjectTemplateSerializer
from .models import Project
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

        return Response({"detail":data})


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
        return Response({"detail":data})

#

        return Response({"detail": data})



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

# class SearchData(ListAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['title', 'description']
# from django.shortcuts import render
#
# # Create your views here.

