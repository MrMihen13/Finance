from django.urls import path

from core import views


urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view()),
    path('category/', views.CategoryCreateApiView.as_view()),
    path('category/<int:pk>', views.CategoryRetrieveUpdateDestroyApiView.as_view()),

    path('costs/', views.CostListApiView.as_view()),
    path('cost/', views.CostCreateApiView.as_view()),
    path('cost/<int:pk>', views.CostRetrieveUpdateDestroyApiView.as_view()),

    path('analitics/manth', views.GetAnalyticsApiView.as_view()),
]
