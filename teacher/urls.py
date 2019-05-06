from django.urls import path 
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index),    
    path('addAttendance/', views.addsheet),    
    path('login/', views.login),
    path('signup/', views.signup),
    path('viewsheet/', views.viewsheet),
    path('fascript/', views.fascript),
    path('temp/', views.temp),
    path('notification/', views.notification),
]

