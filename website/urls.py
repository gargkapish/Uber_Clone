from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rides/', views.rides, name='rides'),
    path('rides/<slug:slug>/', views.ride_detail, name='ride_detail'),
    path('about/', views.about, name='about'),
]