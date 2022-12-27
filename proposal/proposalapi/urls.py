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

    path('get/<str:pk>', views.GetSingle.as_view(), name='get_single'),
    path('get/<str:pk>', views.GetUser.as_view(), name='get_user'),
    path('getuser<str:pk>', views.GetUser.as_view(), name='get_user'),

    path('update/<str:pk>', views.UpdateTodo.as_view(), name='get_update'),
    path('add_todo', views.CreateTask.as_view(), name='add_todo'),
    path('delete_todo/<str:pk>', views.DeleteTodo.as_view(), name='remove todo'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', obtain_auth_token, name="Get Token"),

    path('get', views.SearchData.as_view(), name='Search Data')
]
