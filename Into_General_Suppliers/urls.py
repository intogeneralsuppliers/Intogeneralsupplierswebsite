from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='IGS-Home'),
    path('about/', views.about, name='IGS-About'),
    path('services/', views.services, name='IGS-Services'),
    path('projects/', views.projects, name='IGS-Projects'),
    path('contact/', views.contact, name='IGS-Contact_Now'),
]