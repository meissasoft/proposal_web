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

    path('registerUser', views.RegisterUser.as_view(), name='register'),
    path('updateUser', views.UpdateCurrentUser.as_view(), name='UpdateUser'),
    path('getuserbyid<str:pk>', views.GetUserById.as_view(), name='get_user_by_id'),
    path('get_current_user', views.GetCurrentUser.as_view(), name='get_current_user'),
    path('delete_user/<str:pk>', views.DeleteUser.as_view(), name='Delete_user_by_id'),
    path('filter_user', views.FilterUser.as_view(), name='filter_user'),

    path('login', obtain_auth_token, name="Get Token"),

    path('get', views.SearchData.as_view(), name='Search Data')
]
