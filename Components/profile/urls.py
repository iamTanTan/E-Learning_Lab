from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_detail, name="profile_detail"),
    path('update_profile/', views.update_profile, name="update_profile" ),
]

