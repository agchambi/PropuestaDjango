"""
URL configuration for Examen_php_71524895 project.

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

from django.urls import path
from backend.views import (AutorList, AutorDetail, LibroList, LibroDetail, ClienteList, ClienteDetail, PrestamoList, PrestamoDetail, AutorLibroList, AutorLibroDetail)

urlpatterns = [
    # URLs para Autor
    path('autores/', AutorList.as_view(), name='autor-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),
    
    # URLs para Libro
    path('libros/', LibroList.as_view(), name='libro-list'),
    path('libros/<int:pk>/', LibroDetail.as_view(), name='libro-detail'),
    
    # URLs para Cliente
    path('clientes/', ClienteList.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
    
    # URLs para Prestamo
    path('prestamos/', PrestamoList.as_view(), name='prestamo-list'),
    path('prestamos/<int:pk>/', PrestamoDetail.as_view(), name='prestamo-detail'),
    
    # URLs para AutorLibro
    path('autorlibro/', AutorLibroList.as_view(), name='autorlibro-list'),
    path('autorlibro/<int:pk>/', AutorLibroDetail.as_view(), name='autorlibro-detail'),
]
