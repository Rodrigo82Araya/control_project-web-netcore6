from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('', views.orden_listar, name="orden_listar"),
    path('orden-listar/', views.orden_listar, name="orden_listar"),
    path('orden-agregar/', views.orden_agregar, name="orden_agregar"),
    path('orden-modificar/<id>/', views.orden_modificar, name="orden_modificar"),
    path('orden-eliminar/<id>/', views.orden_eliminar, name="orden_eliminar"),

    # path('seguimiento_listar/<id>/', views.seguimiento_listar, name="seguimiento_listar"),
    # path('seguimiento_agregar/', views.seguimiento_agregar, name="seguimiento_agregar"),
    # path('seguimiento_modificar/<id>/', views.seguimiento_modificar, name="seguimiento_modificar"),

]
