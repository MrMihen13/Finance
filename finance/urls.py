"""
finance URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from counter13_bot import urls as counter13_bot_urls

schema_view = get_swagger_view(title='Finance view')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('counter13_bot/', include(counter13_bot_urls)),
    path('discordbot/', include('discordbot.urls')),
    path('swagger', schema_view),
]
