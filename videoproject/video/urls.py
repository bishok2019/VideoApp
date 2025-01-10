from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('service/', views.video_list, name='video_list'),
    path('like/<int:video_id>/', views.like_video, name='like_video'),
    path('dislike/<int:video_id>/', views.dislike_video, name='dislike_video'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
