"""proector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views

app_name = 'Store'

urlpatterns = [
    path('', views.buy_Skyrim, name = 'home'),
    path('shop/',views.Bethesda, name = 'gone'),
    path("customer/<int:number>", views.Ubisoft, name = 'Ubisoft'),
    path("registration/", views._Registration, name = '_registration' ),
    path("logout/", views.logout_),
    path("login/", views.login_),
    path("categories/", views.show_categories),
    path("<url_slug>", views.separator)
]
