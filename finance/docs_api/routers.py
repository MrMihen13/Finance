from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Finance view')

urlpatterns = [
    path('swagger', schema_view),
    path('core', include('core.urls')),
    path('telegram/api', include('telegram_api.urls')),
]