from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appoinment, name='appoinment'),
    path('blog-sidebar/', views.blog_sidebar, name='blog-sidebar'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('contact/', views.contact, name='contact'),
    path('department/', views.department, name='department'),
    path('department-single/', views.department_single, name='department-single'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctor-single/', views.doctor_single, name='doctor-single'),
    path('documentation/', views.documentation, name='documentation'),
    path('service/', views.service, name='service'),
]