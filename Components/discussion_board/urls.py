from django.urls import path
from . import views

urlpatterns = [
    path('<id_field>/', views.discussions, name='discussions'),
    path('<id_field>/<int:pk>/', views.discussion_detail, name='discussion_detail'),
]