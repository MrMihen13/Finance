from django.urls import path

from core import views


urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view()),
    path('category/add/', views.CreateCategoryApiView.as_view()),
    path('category/retrieve/', views.RetrieveCategoryApiView.as_view()),
    path('costs/', views.CostListApiView.as_view()),
    path('cost/add/', views.CreateCostApiView.as_view()),
    path('cost/retrieve/', views.RetrieveCostApiView.as_view()),
]
