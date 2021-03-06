"""umschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from user import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration, name='register'),
    path('index/', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('profile/', views.profile_view, name='profile'),
    path('editPass/', views.editPass, name='editPass'),
    path('resetNone/', views.resetNone, name='resetNone'),
    path('reset/<slug:token>/', views.reset_password, name='reset'),
    # path('editPass/', views.editPass, name='editPass'),
]
