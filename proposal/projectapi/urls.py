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

    path('createproject', views.CreateProject.as_view(), name='createproject'),

    # path('updateUser', views.UpdateCurrentUser.as_view(), name='UpdateUser'),
    path('getprojectbyid<str:pk>', views.GetProjectById.as_view(), name='Get_Project_By_Id'),
    # path('get_current_user', views.GetCurrentUser.as_view(), name='get_current_user'),
    # path('delete_user/<str:pk>', views.DeleteUser.as_view(), name='Delete_user_by_id'),

    # url for projecttemplate
    path('create_project_ template', views.CreateProjectTemplate.as_view(), name='create_project_template'),

]
