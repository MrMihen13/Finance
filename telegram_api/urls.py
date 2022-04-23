from django.urls import path

from telegram_api import views


urlpatterns = [
    path('cost', views.CostAddCreateDestroyTelegramAPI.as_view()),
    path('costs', views.CostListTelegramAPI.as_view()),
]
