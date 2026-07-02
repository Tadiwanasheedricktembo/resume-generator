from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_resume, name='create_resume'),
    path('success/<int:resume_id>/', views.resume_success, name='resume_success'),
    path('download/<int:resume_id>/', views.download_resume, name='download_resume'),
    path('home/', views.index, name='index'),
]
