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
    path('gear/<int:gear_id>/add_gig/<int:gig_id>/', views.add_gig, name="add_gig"),
    path('gear/<int:gear_id>/remove_gig/<int:gig_id>/', views.remove_gig, name="remove_gig"),


    path('gigs/', views.GigList.as_view(), name="gigs_index"),
    path('gigs/<int:pk>/', views.GigDetail.as_view(), name="gigs_detail"),
    path('gigs/create/', views.GigCreate.as_view(), name="gigs_create"),
    path('gigs/<int:pk>/update/', views.GigUpdate.as_view(), name="gigs_update"),
    path('gigs/<int:pk>/delete/', views.GigDelete.as_view(), name="gigs_delete"),

    path('accounts/signup/', views.signup, name='signup'),

]