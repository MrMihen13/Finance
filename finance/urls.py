"""
finance URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from finance.api import api_v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1)),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
