from django.urls import path
from . import views

urlpatterns = [
    path('<id_field>/', views.discussions, name='discussions'),
    path('<id_field>/<slug:slug>/', views.discussion_detail, name='discussion_detail'),

]