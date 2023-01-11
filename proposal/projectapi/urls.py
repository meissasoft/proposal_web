from django.urls import path,  re_path
from django.conf.urls import url
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin

...

schema_view = get_schema_view(
    openapi.Info(
        title="Proposal API",
        default_version='v1',
        description="Test description",
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
     
     path('admin/', admin.site.urls),
    path(r'^swagger(?P<format>\.json|\.yaml)$',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    # URLs for Project
    path('createproject', views.CreateProject.as_view(), name='createproject'),
    path('listproject', views.ProjectListView.as_view(), name='listproject'),
    path('getprojectbyid<str:pk>', views.GetProjectById.as_view(),
         name='Get_Project_By_Id'),
    path('updateproject/<str:pk>',
         views.UpdateProject.as_view(), name='updateProject'),
    path('delete_project/<str:pk>', views.DeleteProject.as_view(),
         name='Delete_project_by_id'),
    path('get_project_data', views.SearchProjectData.as_view(), name='Project Data'),


    # URLs for Project Template
    path('create_project_template', views.CreateProjectTemplate.as_view(),
         name='create_project_template'),
    path('list_project_template', views.ProjectTemplateListView.as_view(),
         name='list_project_template'),
    path('update_project_template/<str:pk>',
         views.UpdateProjectTemplate.as_view(), name='update_project_template'),
    path('delete_project_template/<str:pk>',
         views.DeleteProjectTemplate.as_view(), name='delete_project_template'),
    path('get_project_template_data',
         views.SearchProjectTemplateData.as_view(), name='Project Template Data'),


    # URLs for Proposal Template
    path('create_proposal_template', views.CreateProposalTemplate.as_view(),
         name='create_proposal_template'),
    path('list_proposal_template', views.ProposalTemplateListView.as_view(),
         name='list_proposal_template'),
    path('update_proposal_template/<str:pk>', views.UpdateProposalTemplate.as_view(),
         name='update_proposal_template'),
    path('delete_proposal_template/<str:pk>', views.DeleteProposalTemplate.as_view(),
         name='delete_proposal_template'),
    path('get_proposal_template_data', views.SearchProposalTemplateData.as_view(
    ), name='Proposal Template Data'),


    # URLs for User Project Template
    path('create_user_project_template', views.CreateUserProjectTemplate.as_view(),
         name='create_user_project_template'),
    path('list_user_project_template', views.UserProjectTemplateListView.as_view(),
         name='list_user_project_template'),
    path('update_user_project_template/<str:pk>', views.UpdateUserProjectTemplate.as_view(),
         name='update_user_project_template'),
    path('delete_user_project_template/<str:pk>', views.DeleteUserProjectTemplate.as_view(),
         name='delete_user_project_template'),
    path('get_user_project_template_data', views.SearchUserProjectTemplateData.as_view(
    ), name='User Project Template Data'),


    # URLs for User Proposal Template
    path('create_user_proposal_template', views.CreateUserProposalTemplate.as_view(),
         name='create_user_proposal_template'),
    path('list_user_proposal_template', views.UserProposalTemplateListView.as_view(),
         name='list_user_proposal_template'),
    path('update_user_proposal_template/<str:pk>', views.UpdateUserProposalTemplate.as_view(),
         name='update_user_proposal_template'),
    path('delete_user_proposal_template/<str:pk>', views.DeleteUserProposalTemplate.as_view(),
         name='delete_user_proposal_template'),
    path('get_user_proposal_template_data', views.SearchUserProposalTemplateData.as_view(
    ), name='User Proposal Template Data'),


    # URLs for JobPost
    path('create_jobpost', views.CreateJobPost.as_view(),
         name='create_jobpost'),
    path('list_jobpost', views.JobPostListView.as_view(),
         name='list_jobpost'),
    path('update_jobpost/<str:pk>', views.UpdateJobPost.as_view(),
         name='update_jobpost'),
    path('delete_jobpost/<str:pk>', views.DeleteJobPost.as_view(),
         name='delete_jobpost'),
    path('get_jobpost_data', views.SearchJobPostData.as_view(), name='JobPost Data'),


    path('ProposalTemplateCreate', views.ProposalTemplateCreate.as_view(),
         name='ProposalTemplateCreate'),
    
     # URLs for Attribute
    path('create_attribute', views.CreateAttribute.as_view(),
         name='create_attribute'),
    path('list_attribute', views.AttributeListView.as_view(),
         name='list_attribute'),
    path('update_attribute/<str:pk>', views.UpdateAttribute.as_view(),
         name='update_attribute'),
    path('delete_attribute/<str:pk>', views.DeleteAttribute.as_view(),
         name='delete_attribute'),
    path('get_attribute_data', views.SearchAttribute.as_view(), name='Attribute Data'),

     # URLs for User Attribute
    path('create_user_attribute', views.CreateUserAttribute.as_view(),
         name='create_user_attribute'),
    path('list_user_attribute', views.UserAttributeListView.as_view(),
         name='list_user_attribute'),
    path('update_user_attribute/<str:pk>', views.UpdateUserAttribute.as_view(),
         name='update_user_attribute'),
    path('delete_user_attribute/<str:pk>', views.DeleteUserAttribute.as_view(),
         name='delete_user_attribute'),
    path('get_user_attribute_data', views.SearchUserAttribute.as_view(), name='User Attribute Data'),

     # URLs for Project Attribute
    path('create_project_attribute', views.CreateProjectAttribute.as_view(),
         name='create_project_attribute'),
    path('list_project_attribute', views.ProjectAttributeListView.as_view(),
         name='list_project_attribute'),
    path('update_project_attribute/<str:pk>', views.UpdateProjectAttribute.as_view(),
         name='update_project_attribute'),
    path('delete_project_attribute/<str:pk>', views.DeleteProjectAttribute.as_view(),
         name='delete_project_attribute'),
    path('get_project_attribute_data', views.SearchProjectAttribute.as_view(), name='Project Attribute Data'),
]
