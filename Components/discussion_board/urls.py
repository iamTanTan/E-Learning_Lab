from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiscussionList.as_view(), name='discussion'),
    path('<slug:slug>/', views.discussion_detail, name='discussion_detail'),

]