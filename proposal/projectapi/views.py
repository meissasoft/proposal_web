from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProjectSerializer
from .models import Project
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView



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
#

class GetProjectById(APIView):
    serializer_class = ProjectSerializer
    allowed_methods = ('GET',)

    def get(self,request,pk,*args, **kwargs):
        try:
            get_project = Project.objects.get(id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Project not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(get_project)
        return Response(serializer.data)
#
#
# class GetCurrentUser(APIView):
#     serializer_class = RegisterSerializer
#     allowed_methods = ('POST',)
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request,*args, **kwargs):
#         try:
#             current_user_id = request.user.id
#             print(current_user_id)
#             get_user = UserRegistration.objects.get(id=current_user_id)
#         except Exception as e:
#             print("error", e)
#             return Response({"Error": "This User not found"}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = RegisterSerializer(get_user)
#         return Response(serializer.data)
#
# class UpdateCurrentUser(UpdateAPIView):
#     serializer_class = UpdateRegisterSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     allowed_methods = ('PUT',)
#     parser_classes = [MultiPartParser, FormParser]
#
#     def update(self, request, *args, **kwargs):
#         current_user_id = request.user.id
#         print(current_user_id)
#         kwargs['partial'] = True
#         # user_obj = UserRegistration.objects.get(id= current_user_id)
#         # print(user_obj.email)
#         try:
#             user_obj = UserRegistration.objects.get(id=current_user_id)
#             print(user_obj.id)
#             print(user_obj.email)
#
#         except Exception as e:
#             print("error", e)
#             return Response({"Error": "This Todo not found"}, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = UpdateRegisterSerializer(instance=user_obj,  data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class DeleteUser(CreateAPIView):
#     allowed_methods = ('DELETE',)
#
#     def delete(self, request, pk):
#         try:
#             get_user_obj = UserRegistration.objects.get(id=pk)
#         except Exception as e:
#             print("error", e)
#             return Response({"Error": "This User not found"}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = RemoveUserSerializer(get_user_obj)
#
#         get_user_obj.delete()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
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
