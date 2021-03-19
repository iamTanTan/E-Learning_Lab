from django.urls import path
from . import views

urlpatterns = [
    path('<id_field>/', views.discussions, name='discussions'),
    path('<id_field>/<int:pk>/', views.discussion_detail, name='discussion_detail'),
    path('<int:pk>/update_comment', views.update_comment, name='update_comment'),
    path('<int:pk>/delete_comment', views.delete_own_comment, name='delete_own_comment'),
    path('<int:pk>/delete_reply', views.delete_own_reply, name='delete_own_reply'),
]