from django.urls import path
from . import views

app_name = 'kiosk'

urlpatterns = [
    path('', views.MenuListView.as_view(), name='index'),
    path('item/<int:pk>/', views.MenuDetailView.as_view(), name='detail'),
    path('item/<int:pk>/delete/', views.MenuDeleteView.as_view(), name='delete'),
]