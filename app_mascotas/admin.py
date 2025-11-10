from django.contrib import admin
from .models import Animal, Cliente, Empleado

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id_animales', 'nombre', 'especie', 'edad', 'dueno']
    list_filter = ['especie', 'dueno']
    search_fields = ['nombre', 'especie']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id_cliente', 'nombre', 'apepaterno', 'correo', 'telefono']
    search_fields = ['nombre', 'apepaterno', 'correo']

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id_empleado', 'nombre', 'apepaterno', 'ocupacion', 'telefono']
    search_fields = ['nombre', 'apepaterno', 'ocupacion']