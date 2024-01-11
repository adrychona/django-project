"""
URL configuration for ProjectOne project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import *
#Ways to import
#1. import projectOne.views
#2. import projectOne.views as pviews
#3. from .views import hora_actual
urlpatterns = [
    path('admin/', admin.site.urls),
    path("bienvenida/", bienvenida), #1. projectOne.views.bienvenida
    path("portal/", solicitudes), #2. pviews.solicitudes
    path("now/", hora_actual), #3 hora_actual
    path("hola/<nombre>", saludar), #Lo que escriba el usuario despues del hola/ sera tomado como el parametro nombre de la funcion saludar.
    path("inicio/", inicio)
]
