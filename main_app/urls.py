from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gear/', views.gear_index, name="index"),
    path('gear/<int:gear_id>/', views.gear_detail, name='detail'),
    path('gear/<int:gear_id>/add_service/', views.add_service, name='add_service'),
    path('gear/create/', views.GearCreate.as_view(), name="gear_create"),
    path('gear/<int:pk>/update/', views.GearUpdate.as_view(), name="gear_update"),
    path('gear/<int:pk>/delete/', views.GearDelete.as_view(), name="gear_delete"),
]