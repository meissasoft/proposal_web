from django.urls import path,  re_path
from django.conf.urls import url
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token

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
    path(r'^swagger(?P<format>\.json|\.yaml)$',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    # URLs for Project
    path('createproject', views.CreateProject.as_view(), name='createproject'),
    path('listproject', views.ProjectListView.as_view(), name='listproject'),
    path('getprojectbyid<str:pk>', views.GetProjectById.as_view(),
         name='Get_Project_By_Id'),
    path('updateproject<str:pk>',
         views.UpdateProject.as_view(), name='updateProject'),
    path('delete_project/<str:pk>', views.DeleteProject.as_view(),
         name='Delete_project_by_id'),

    # URLs for Project Template
    path('create_project_template', views.CreateProjectTemplate.as_view(),
         name='create_project_template'),
    path('list_project_template', views.ProjectTemplateListView.as_view(),
         name='list_project_template'),
    path('update_project_template<str:pk>',
         views.UpdateProjectTemplate.as_view(), name='update_project_template'),
    path('delete_project_template/<str:pk>',
         views.DeleteProjectTemplate.as_view(), name='delete_project_template'),

    # URLs for Proposal Template
    path('create_proposal_template', views.CreateProposalTemplate.as_view(),
         name='create_proposal_template'),
    path('list_proposal_template', views.ProposalTemplateListView.as_view(),
         name='list_proposal_template'),
    path('update_proposal_template', views.UpdateProposalTemplate.as_view(),
         name='update_proposal_template'),
    path('delete_proposal_template', views.DeleteProposalTemplate.as_view(),
         name='delete_proposal_template'),
]
