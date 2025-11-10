:

# 🔧 Paso 1: Realizar las migraciones
    Terminal:

    bash
    # Crear migraciones
    python manage.py makemigrations

    # Aplicar migraciones
    python manage.py migrate

# 🔧 Paso 2: Crear las vistas para Empleados
    app_mascotas/views.py (AGREGAR estas funciones al final):

    python
        
        # ==========================================
    # VISTAS PARA EMPLEADOS
    # ==========================================

    def inicio_empleados(request):
    return render(request, 'empleados/inicio_empleados.html')

    def agregar_empleado(request):
    if request.method == 'POST':
        # Crear nuevo empleado con datos del formulario
        nuevo_empleado = Empleado(
            nombre=request.POST['nombre'],
            apepaterno=request.POST['apepaterno'],
            apematerno=request.POST['apematerno'],
            telefono=request.POST['telefono'],
            domicilio=request.POST['domicilio'],
            ocupacion=request.POST['ocupacion'],
            alergias=request.POST['alergias']
        )
        nuevo_empleado.save()
        return redirect('ver_empleados')
    
    return render(request, 'empleados/agregar_empleados.html')

    def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

    def actualizar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    return render(request, 'empleados/actualizar_empleados.html', {'empleado': empleado})

    def realizar_actualizacion_empleado(request, id_empleado):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
        empleado.nombre = request.POST['nombre']
        empleado.apepaterno = request.POST['apepaterno']
        empleado.apematerno = request.POST['apematerno']
        empleado.telefono = request.POST['telefono']
        empleado.domicilio = request.POST['domicilio']
        empleado.ocupacion = request.POST['ocupacion']
        empleado.alergias = request.POST['alergias']
        empleado.save()
        return redirect('ver_empleados')
    
    return redirect('ver_empleados')

    def borrar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    
    return render(request, 'empleados/borrar_empleados.html', {'empleado': empleado})
# 🔧 Paso 3: Actualizar el navbar
app_mascotas/templates/navbar.html (MODIFICAR la sección de Empleados):

    html
    <nav class="navbar navbar-expand-lg navbar-dark navbar-custom mb-4 rounded">
    <div class="container">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'inicio_mascotas' %}">
                        🏠 Inicio
                    </a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                        🐶 Mascotas
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="{% url 'agregar_mascota' %}">Agregar mascotas</a></li>
                        <li><a class="dropdown-item" href="{% url 'ver_mascotas' %}">Ver mascotas</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                        👥 Clientes
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="{% url 'inicio_clientes' %}">Inicio clientes</a></li>
                        <li><a class="dropdown-item" href="{% url 'agregar_cliente' %}">Agregar clientes</a></li>
                        <li><a class="dropdown-item" href="{% url 'ver_clientes' %}">Ver clientes</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                        👨‍💼 Empleados
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="{% url 'inicio_empleados' %}">Inicio empleados</a></li>
                        <li><a class="dropdown-item" href="{% url 'agregar_empleado' %}">Agregar empleados</a></li>
                        <li><a class="dropdown-item" href="{% url 'ver_empleados' %}">Ver empleados</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
    </nav>

# 🔧 Paso 4: Agregar URLs para Empleados
    
    app_mascotas/urls.py (MODIFICAR agregando las rutas de empleados):

    python
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
# 🔧 Paso 5: Registrar modelos en admin (ya está hecho)

    app_mascotas/admin.py (YA DEBERÍA ESTAR CONFIGURADO):

    python
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

## 🔧 Paso 6: Crear las plantillas para Empleados

# app_mascotas/templates/empleados/inicio_empleados.html (CREAR):

    html
    {% extends 'base.html' %}

    {% block content %}
    <div class="row">
    <div class="col-md-8">
        <div class="card shadow-sm">
            <div class="card-body">
                <h2 class="card-title text-primary">👨‍💼 Gestión de Empleados</h2>
                <p class="card-text">
                    Sistema de administración para la gestión integral del personal de la veterinaria. 
                    Aquí podrás realizar todas las operaciones CRUD necesarias para el correcto 
                    funcionamiento del establecimiento.
                </p>
                <h5 class="mt-4">Funcionalidades principales:</h5>
                <ul>
                    <li>Registro de nuevos empleados</li>
                    <li>Consulta de información del personal</li>
                    <li>Actualización de datos laborales</li>
                    <li>Gestión de asignación de mascotas</li>
                    <li>Control de alergias y restricciones</li>
                </ul>
                <div class="mt-4">
                    <a href="{% url 'agregar_empleado' %}" class="btn btn-primary me-2">➕ Agregar Empleado</a>
                    <a href="{% url 'ver_empleados' %}" class="btn btn-success">📋 Ver Empleados</a>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card shadow-sm">
            <div class="card-body text-center">
                <img src="https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" 
                     alt="Empleados" class="img-fluid rounded">
                <h5 class="mt-3">Equipo Profesional</h5>
                <p class="text-muted">Nuestro personal capacitado</p>
            </div>
        </div>
    </div>
    </div>
    {% endblock %}

# app_mascotas/templates/empleados/agregar_empleados.html (CREAR):

    html
    {% extends 'base.html' %}

    {% block content %}
    <div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card shadow-sm">
            <div class="card-header bg-primary text-white">
                <h4 class="mb-0">➕ Agregar Nuevo Empleado</h4>
            </div>
            <div class="card-body">
                <form method="POST">
                    {% csrf_token %}
                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Nombre</label>
                            <input type="text" class="form-control" name="nombre" required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Apellido Paterno</label>
                            <input type="text" class="form-control" name="apepaterno" required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Apellido Materno</label>
                            <input type="text" class="form-control" name="apematerno" required>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Teléfono</label>
                            <input type="text" class="form-control" name="telefono" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Ocupación</label>
                            <input type="text" class="form-control" name="ocupacion" required>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Domicilio</label>
                        <textarea class="form-control" name="domicilio" rows="2" placeholder="Dirección completa..."></textarea>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Alergias</label>
                        <textarea class="form-control" name="alergias" rows="3" placeholder="Alergias conocidas del empleado..."></textarea>
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <button type="submit" class="btn btn-primary me-md-2">Guardar Empleado</button>
                        <a href="{% url 'ver_empleados' %}" class="btn btn-secondary">Cancelar</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>
    {% endblock %}

# app_mascotas/templates/empleados/ver_empleados.html (CREAR):

    html
  
      {% extends 'base.html' %}

    {% block content %}
    <div class="card shadow-sm">
    <div class="card-header bg-success text-white d-flex justify-content-between align-items-center">
        <h4 class="mb-0">📋 Lista de Empleados</h4>
        <a href="{% url 'agregar_empleado' %}" class="btn btn-light btn-sm">➕ Agregar Nuevo</a>
    </div>
    <div class="card-body">
        {% if empleados %}
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Apellidos</th>
                        <th>Ocupación</th>
                        <th>Teléfono</th>
                        <th>Domicilio</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {% for empleado in empleados %}
                    <tr>
                        <td>{{ empleado.id_empleado }}</td>
                        <td><strong>{{ empleado.nombre }}</strong></td>
                        <td>{{ empleado.apepaterno }} {{ empleado.apematerno }}</td>
                        <td>
                            <span class="badge bg-info">{{ empleado.ocupacion }}</span>
                        </td>
                        <td>{{ empleado.telefono }}</td>
                        <td>{{ empleado.domicilio|default:"-"|truncatewords:5 }}</td>
                        <td>
                            <a href="#" class="btn btn-info btn-sm">👁️ Ver</a>
                            <a href="{% url 'actualizar_empleado' empleado.id_empleado %}" class="btn btn-warning btn-sm">✏️ Editar</a>
                            <a href="{% url 'borrar_empleado' empleado.id_empleado %}" class="btn btn-danger btn-sm">🗑️ Borrar</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% else %}
        <div class="alert alert-info text-center">
            <h5>No hay empleados registrados</h5>
            <p>Comienza agregando el primer empleado al sistema.</p>
            <a href="{% url 'agregar_empleado' %}" class="btn btn-primary">Agregar Primer Empleado</a>
        </div>
        {% endif %}
    </div>
      </div>
      {% endblock %}

# app_mascotas/templates/empleados/actualizar_empleados.html (CREAR):

    html
      
      {% extends 'base.html' %}

    {% block content %}
    <div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card shadow-sm">
            <div class="card-header bg-warning text-dark">
                <h4 class="mb-0">✏️ Actualizar Empleado: {{ empleado.nombre }}</h4>
            </div>
            <div class="card-body">
                <form method="POST" action="{% url 'realizar_actualizacion_empleado' empleado.id_empleado %}">
                    {% csrf_token %}
                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Nombre</label>
                            <input type="text" class="form-control" name="nombre" value="{{ empleado.nombre }}" required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Apellido Paterno</label>
                            <input type="text" class="form-control" name="apepaterno" value="{{ empleado.apepaterno }}" required>
                        </div>
                        <div class="col-md-4 mb-3">
                            <label class="form-label">Apellido Materno</label>
                            <input type="text" class="form-control" name="apematerno" value="{{ empleado.apematerno }}" required>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Teléfono</label>
                            <input type="text" class="form-control" name="telefono" value="{{ empleado.telefono }}" required>
                        </div>
                        <div class="col-md-6 mb-3">
                            <label class="form-label">Ocupación</label>
                            <input type="text" class="form-control" name="ocupacion" value="{{ empleado.ocupacion }}" required>
                        </div>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Domicilio</label>
                        <textarea class="form-control" name="domicilio" rows="2">{{ empleado.domicilio }}</textarea>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Alergias</label>
                        <textarea class="form-control" name="alergias" rows="3">{{ empleado.alergias }}</textarea>
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <button type="submit" class="btn btn-warning me-md-2">Actualizar Empleado</button>
                        <a href="{% url 'ver_empleados' %}" class="btn btn-secondary">Cancelar</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>
    {% endblock %}

# app_mascotas/templates/empleados/borrar_empleados.html (CREAR):

    html

    {% extends 'base.html' %}
  
    {% block content %}
    <div class="row justify-content-center">
    <div class="col-md-6">
        <div class="card shadow-sm">
            <div class="card-header bg-danger text-white">
                <h4 class="mb-0">🗑️ Confirmar Eliminación</h4>
            </div>
            <div class="card-body text-center">
                <div class="alert alert-warning">
                    <h5>¿Estás seguro de que quieres eliminar este empleado?</h5>
                    <p class="mb-1"><strong>Nombre:</strong> {{ empleado.nombre }}</p>
                    <p class="mb-1"><strong>Apellidos:</strong> {{ empleado.apepaterno }} {{ empleado.apematerno }}</p>
                    <p class="mb-1"><strong>Ocupación:</strong> {{ empleado.ocupacion }}</p>
                    <p class="mb-3"><strong>ID:</strong> {{ empleado.id_empleado }}</p>
                    <p class="text-danger"><strong>⚠️ Esta acción no se puede deshacer</strong></p>
                </div>
                
                <form method="POST">
                    {% csrf_token %}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-center">
                        <button type="submit" class="btn btn-danger me-md-2">Sí, Eliminar</button>
                        <a href="{% url 'ver_empleados' %}" class="btn btn-secondary">Cancelar</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>
    {% endblock %}

# 🔧 Paso 7: Estructura final de carpetas


    UIII_mascotas_0237/
    ├── .venv/
    ├── backend_mascotas/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── app_mascotas/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── header.html
    │   │   ├── navbar.html
    │   │   ├── footer.html
    │   │   ├── inicio.html
    │   │   ├── mascotas/
    │   │   │   ├── agregar_mascotas.html
    │   │   │   ├── ver_mascotas.html
    │   │   │   ├── actualizar_mascotas.html
    │   │   │   ├── borrar_mascotas.html
    │   │   │   └── detalle_mascota.html
    │   │   ├── clientes/
    │   │   │   ├── inicio_clientes.html
    │   │   │   ├── agregar_clientes.html
    │   │   │   ├── ver_clientes.html
    │   │   │   ├── actualizar_clientes.html
    │   │   │   └── borrar_clientes.html
    │   │   └── empleados/                    # NUEVA CARPETA
    │   │       ├── inicio_empleados.html
    │   │       ├── agregar_empleados.html
    │   │       ├── ver_empleados.html
    │   │       ├── actualizar_empleados.html
    │   │       └── borrar_empleados.html
    ├── manage.py
    └── requirements.txt

# 🚀 Paso 8: Ejecutar migraciones y servidor
Terminal:


    
    # Crear migraciones para los cambios
    python manage.py makemigrations

    # Aplicar migraciones
    python manage.py migrate

    # Ejecutar servidor en puerto 8037
    python manage.py runserver 8037

# ✅ Proyecto Completamente Funcional

    Accesos:

    http://127.0.0.1:8037/ - Inicio mascotas

    http://127.0.0.1:8037/clientes/ - Gestión de clientes

    http://127.0.0.1:8037/empleados/ - Gestión de empleados

    http://127.0.0.1:8037/admin/ - Panel de administración

