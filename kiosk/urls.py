from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuListView.as_view(), name='index'),
    path('item/<int:pk>/', views.MenuDetailView.as_view(), name='detail'),
]