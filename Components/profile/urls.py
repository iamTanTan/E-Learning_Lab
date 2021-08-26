from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_detail, name="profile_detail"),
    path('update_profile/', views.update_profile, name="update_profile"),    
    path('enroll_in_course/<course_id>/', views.enroll_in_course, name="enroll"),
    path('unenroll_from_course/<course_id>/', views.unenroll_from_course, name="unenroll"),
    
]

