"""
URL configuration for Orellana_Alonso_FINAL project.

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
from .views import HomePageView, InscritoCreateView
from .api_views import InscritoListCreateView, InscritoDetailView, InstitucionListCreateView, InstitucionDetailView, author_info

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('inscritos/', InscritoListCreateView.as_view(), name='inscrito-list-create'),
    path('inscritos/<int:pk>/', InscritoDetailView.as_view(), name='inscrito-detail'),
    path('instituciones/', InstitucionListCreateView.as_view(), name='institucion-list-create'),
    path('instituciones/<int:pk>/', InstitucionDetailView.as_view(), name='institucion-detail'),
    path('inscrito/nuevo/', InscritoCreateView.as_view(), name='inscrito-create'),
    path('institucion/nueva/', InstitucionCreateView.as_view(), name='institucion-create'),
    path('api/author/', AuthorInfoView.as_view(), name='author-info'),
      
    ]
      
    








