from django.urls import path

from core import views


urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view()),
    path('category/', views.CategoryRetrieveUpdateDestroyApiView.as_view()),
    path('costs/', views.CostListApiView.as_view()),
    path('cost/', views.CostRetrieveUpdateDestroyApiView.as_view()),
]
