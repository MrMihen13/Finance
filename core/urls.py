from django.urls import path, re_path

from core import views

urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view()),
    path('category/', views.CategoryCreateApiView.as_view()),
    path('category/<int:pk>', views.CategoryRetrieveUpdateDestroyApiView.as_view()),

    path('costs/', views.CostListApiView.as_view()),
    path('costs/<int:month>/<int:year>/', views.CostListApiView.as_view()),
    path('costs/export/', views.ExelExportApiView.as_view()),
    path('costs/export/<int:month>/<int:year>/', views.ExelExportApiView.as_view()),
    path('cost/', views.CostCreateApiView.as_view()),
    path('cost/<int:pk>', views.CostRetrieveUpdateDestroyApiView.as_view()),

    path('analytics/', views.GetAnalyticsApiView.as_view()),
    path('analytics/<int:month>/<int:year>/', views.GetAnalyticsApiView.as_view())
]
