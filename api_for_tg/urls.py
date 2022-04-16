from django.urls import path

from api_for_tg import views


urlpatterns = [
    path('add_cost', views.AddCostTelegramAPI.as_view()),
    path('list', views.CostListTelegramAPI.as_view()),
]
