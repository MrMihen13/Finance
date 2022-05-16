from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Finance API",
        default_version='v1',
        description="Test description",
        contact=openapi.Contact(email="krpohg@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='chema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='chema-redoc'),
    path('', include('core.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('telegram/', include('telegram_api.urls')),
]
