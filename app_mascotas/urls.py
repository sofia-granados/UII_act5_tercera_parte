from django.urls import path
from . import views

urlpatterns = [
    # URLs para Mascotas
    path('', views.inicio_mascotas, name='inicio_mascotas'),
    path('agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('ver/', views.ver_mascotas, name='ver_mascotas'),
    path('detalle/<int:id_animales>/', views.ver_detalle_mascota, name='detalle_mascota'),
    path('actualizar/<int:id_animales>/', views.actualizar_mascota, name='actualizar_mascota'),
    path('realizar-actualizacion/<int:id_animales>/', views.realizar_actualizacion_mascota, name='realizar_actualizacion_mascota'),
    path('borrar/<int:id_animales>/', views.borrar_mascota, name='borrar_mascota'),
    
    # URLs para Clientes
    path('clientes/', views.inicio_clientes, name='inicio_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_clientes, name='ver_clientes'),
        # En el patterns array, agregar esta línea en la sección de clientes:
    path('clientes/detalle/<int:id_cliente>/', views.ver_detalle_cliente, name='detalle_cliente'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar-actualizacion/<int:id_cliente>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),

    
    # NUEVAS URLs para Empleados
    path('empleados/', views.inicio_empleados, name='inicio_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/ver/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/<int:id_empleado>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/realizar-actualizacion/<int:id_empleado>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleados/borrar/<int:id_empleado>/', views.borrar_empleado, name='borrar_empleado'),
]