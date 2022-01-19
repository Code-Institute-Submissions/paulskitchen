"""paulskitchen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.urls import re_path
from django.views.static import serve
from restaurant import views as restaurant_views
from .settings import STATIC_ROOT

urlpatterns = [
    path('', restaurant_views.index),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', restaurant_views.profile),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}), 
    path('contact/', restaurant_views.contact, name="contact"),
    path('menu/', restaurant_views.menu, name="menu"),
    path('create_booking/', restaurant_views.create_booking, name="booking_form"),
    path('about/', restaurant_views.about, name="about"),
    path('contact_create/', restaurant_views.contact_create_view, name="contact_create"),
    path('manage_bookings/', restaurant_views.manage_bookings, name="manage_bookings"),
    path('delete_booking/<int:booking_id>', restaurant_views.delete_booking, name="delete_booking"),
    path('deletion_confirmation/', restaurant_views.deletion_confirmation, name="deletion_confirmation"),
]
