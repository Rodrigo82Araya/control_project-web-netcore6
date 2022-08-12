from django.urls import URLPattern, path
from . import views

urlpatterns =[
    #ORDEN====================================
    path('', views.orden_listar, name="orden_listar"),
    path('orden-listar/', views.orden_listar, name="orden_listar"),
    path('orden-agregar/', views.orden_agregar, name="orden_agregar"),
    path('orden-modificar/<id>/', views.orden_modificar, name="orden_modificar"),
    path('orden-eliminar/<id>/', views.orden_eliminar, name="orden_eliminar"),

    #SEGUIMIENTO====================================
    path('orden-listar/<id>/seguimiento-listar/', views.seguimiento_listar, name="seguimiento_listar"),
    path('orden-listar/<idOrden>/seguimiento-agregar/', views.seguimiento_agregar, name="seguimiento_agregar"),
    path('seguimiento-modificar/<id>/', views.seguimiento_modificar, name="seguimiento_modificar"),
    path('seguimiento-eliminar/<id>/', views.seguimiento_eliminar, name="seguimiento_eliminar"),

    #AVANCES=========================================
    #path('seguimiento-listar/<id>/avance-listar/', views.seguimiento_listar, name="avance_listar"),
]
