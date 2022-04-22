from django.urls import path

from telegram_api import views


urlpatterns = [
    path('add_cost', views.AddCostTelegramAPI.as_view()),
    path('list', views.CostListTelegramAPI.as_view()),
]
