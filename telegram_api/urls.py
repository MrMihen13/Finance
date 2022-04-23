from django.urls import path

from telegram_api import views


urlpatterns = [
    path('cost', views.AddCostTelegramAPI.as_view()),
    path('costs', views.CostListTelegramAPI.as_view()),
]
