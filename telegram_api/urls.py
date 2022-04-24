from django.urls import path, re_path

from telegram_api import views


urlpatterns = [
    path('cost/<int:pk>', views.CostRetrieveUpdateDestroyTelegramAPI.as_view()),
    path('cost/', views.CostCreateTelegramAPI.as_view()),
    path('costs/', views.CostListTelegramAPI.as_view()),
    path('category/<int:pk>', views.CategoryRetrieveUpdateDestroyTelegramAPI.as_view()),
    path('category/', views.CategoryCreateTelegramAPI.as_view()),
    path('categores/', views.CategoryListTelegramAPI.as_view()),
]
