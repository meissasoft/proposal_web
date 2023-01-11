from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import AttributeSerializer, JobPostSerializer, ProjectAttributeSerializer, ProjectSerializer, ProjectTemplateSerializer, ProposalTemplateSerializer, UserAttributeSerializer, \
    UserProjectTemplateSerializer, UserProposalTemplateSerializer, CreateProposalTemplateSerializer
from .models import Attribute, JobPost, Project, ProjectAttribute, ProjectTemplate, ProposalTemplate, UserAttribute, UserProjectTemplate, UserProposaltemplate
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter
from proposalapi.models import UserRegistration
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


class SearchProjectData(ListAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'languages', 'platform', 'project_earning']

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
    filter_backends = [SearchFilter]
    search_fields = ['name', 'content', 'status']

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


class SearchProjectTemplateData(ListAPIView):

    queryset = ProjectTemplate.objects.all()
    serializer_class = ProjectTemplateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'content', 'status']


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


class SearchProposalTemplateData(ListAPIView):

    queryset = ProposalTemplate.objects.all()
    serializer_class = ProposalTemplateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'content', 'status']

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


class SearchUserProjectTemplateData(ListAPIView):

    queryset = UserProjectTemplate.objects.all()
    serializer_class = UserProjectTemplateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user_id']

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
    filter_backends = [SearchFilter]
    search_fields = ['user_id']

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


class SearchUserProposalTemplateData(ListAPIView):

    queryset = UserProposaltemplate.objects.all()
    serializer_class = UserProposalTemplateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user_id']


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


class SearchJobPostData(ListAPIView):

    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['proposal_template_id', 'project_id', 'user_id']


class ProposalTemplateCreate(CreateAPIView):
    serializer_class = CreateProposalTemplateSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        user_id = request.data['userID']
        projectIds = request.data['projectIds']
        project_ids = projectIds.split(",")
        proposal_tempalte_id = request.data['proposal_tempalte_id']
        project_template_id = request.data["project_template_id"]

        projects_list = []
        for project in project_ids:
            project_obj = Project.objects.get(id=project)
            if project_obj:
                project_template_obj = ProjectTemplate.objects.get(
                    id=project_template_id)
                if project_template_obj:
                    project_template_content = project_template_obj.content
                    char_to_replace = {
                        'project_name': project_obj.name, 'project_url': project_obj.project_url_link, }

                    for key, value in char_to_replace.items():
                        # Replace key character with value character in string
                        project_template_content = project_template_content.replace(
                            key, value)

                    projects_list.append(project_template_content + "\n")

                else:
                    return Response({"message": f"project template not found against this project_template_id  {project_template_id}"})

            else:
                return Response({"message": f"project not found against this project_id {project}"})

        user_obj = UserRegistration.objects.get(id=user_id)
        if user_obj:

            proposal_tempalte_obj = ProposalTemplate.objects.get(
                id=proposal_tempalte_id)
            if proposal_tempalte_obj:
                proposal_tempalte_content = proposal_tempalte_obj.content
                projects = " "

                char_to_replace = {'UserName': user_obj.username, 'Title': user_obj.stack, "Stack": "Full stack", "Languages": user_obj.languages,
                                   "Projects": projects.join(projects_list), "Username": user_obj.username}
                for key, value in char_to_replace.items():
                    # Replace key character with value character in string
                    proposal_tempalte_content = proposal_tempalte_content.replace(
                        key, value)

                return Response({"detail": proposal_tempalte_content})
            else:
                return Response(
                    {"message": f"proposal template not found against this proposal_template_id  {proposal_tempalte_id}"})

        else:
            return Response({"message": f"user not found against this id {user_id}"})


# Attribute CRUD
class CreateAttribute(CreateAPIView):
    serializer_class = AttributeSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        serializer = AttributeSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            attribute = serializer.save()
            data['name'] = attribute.name
        else:
            data = serializer.errors
            print('Error', data.keys())
        return Response({"detail": data})


class AttributeListView(ListAPIView):
    serializer_class = AttributeSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_Attribute = Attribute.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AttributeSerializer(
            get_Attribute, many=True)
        return Response(serializer.data)


class UpdateAttribute(UpdateAPIView):
    serializer_class = AttributeSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            attribute_obj = Attribute.objects.get(id=pk)
            print(attribute_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AttributeSerializer(
            instance=attribute_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAttribute(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_attribute_obj = Attribute.objects.get(
                id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AttributeSerializer(
            get_attribute_obj)
        get_attribute_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchAttribute(ListAPIView):

    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


# User Attribute CRUD
class CreateUserAttribute(CreateAPIView):
    serializer_class = UserAttributeSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        serializer = UserAttributeSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user_attribute = serializer.save()
            data['user'] = user_attribute.user
            data['attribute_value'] = user_attribute.attribute_value
        else:
            data = serializer.errors
            print('Error', data.keys())
        return Response({"detail": data})


class UserAttributeListView(ListAPIView):
    serializer_class = UserAttributeSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_User_Attribute = UserAttribute.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "This User Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserAttributeSerializer(
            get_User_Attribute, many=True)
        return Response(serializer.data)


class UpdateUserAttribute(UpdateAPIView):
    serializer_class = UserAttributeSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            user_attribute_obj = UserAttribute.objects.get(id=pk)
            print(user_attribute_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This User Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserAttributeSerializer(
            instance=user_attribute_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserAttribute(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_user_attribute_obj = UserAttribute.objects.get(
                id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This User Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserAttributeSerializer(
            get_user_attribute_obj)
        get_user_attribute_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchUserAttribute(ListAPIView):

    queryset = UserAttribute.objects.all()
    serializer_class = UserAttributeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user']


# Project Attribute CRUD
class CreateProjectAttribute(CreateAPIView):
    serializer_class = ProjectAttributeSerializer
    allowed_methods = ('POST',)

    def post(self, request, format=None):
        serializer = ProjectAttributeSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            project_attribute = serializer.save()
            data['project'] = project_attribute.project
            data['attribute_value'] = project_attribute.attribute_value
        else:
            data = serializer.errors
            print('Error', data.keys())
        return Response({"detail": data})


class ProjectAttributeListView(ListAPIView):
    serializer_class = ProjectAttributeSerializer
    allowed_methods = ('GET',)

    def get(self, request, *args, **kwargs):
        try:
            get_Project_Attribute = ProjectAttribute.objects.all()
        except Exception as e:
            print("error", e)
            return Response({"Error": "Project Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectAttributeSerializer(
            get_Project_Attribute, many=True)
        return Response(serializer.data)


class UpdateProjectAttribute(UpdateAPIView):
    serializer_class = ProjectAttributeSerializer
    allowed_methods = ('PUT',)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        try:
            project_attribute_obj = ProjectAttribute.objects.get(id=pk)
            print(project_attribute_obj.id)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Project Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectAttributeSerializer(
            instance=project_attribute_obj,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProjectAttribute(DestroyAPIView):
    allowed_methods = ('DELETE',)

    def delete(self, request, pk):
        try:
            get_project_attribute_obj = ProjectAttribute.objects.get(
                id=pk)
        except Exception as e:
            print("error", e)
            return Response({"Error": "This Project Attribute was not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserAttributeSerializer(
            get_project_attribute_obj)
        get_project_attribute_obj.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchProjectAttribute(ListAPIView):

    queryset = ProjectAttribute.objects.all()
    serializer_class = ProjectAttributeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['project']
