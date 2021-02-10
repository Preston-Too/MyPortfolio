from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_me, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    
]