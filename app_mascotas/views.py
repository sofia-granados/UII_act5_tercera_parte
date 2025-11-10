from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal, Cliente, Empleado

def inicio_mascotas(request):
    return render(request, 'inicio.html')

def agregar_mascota(request):
    if request.method == 'POST':
        # Crear nueva mascota con datos del formulario
        nueva_mascota = Animal(
            nombre=request.POST['nombre'],
            edad=request.POST['edad'],
            peso=request.POST['peso'],
            cuidados=request.POST['cuidados'],
            enfermedades=request.POST['enfermedades'],
            especie=request.POST['especie'],
            alimentacion=request.POST['alimentacion']
        )
        
        # Asignar dueño si se seleccionó uno
        dueno_id = request.POST.get('dueno')
        if dueno_id:
            try:
                dueno = Cliente.objects.get(id_cliente=dueno_id)
                nueva_mascota.dueno = dueno
            except Cliente.DoesNotExist:
                pass  # Si el cliente no existe, continuar sin dueño
        
        # Manejar la imagen si se proporciona
        if 'imagen' in request.FILES:
            nueva_mascota.imagen = request.FILES['imagen']
            
        nueva_mascota.save()
        return redirect('ver_mascotas')

    # Obtener lista de clientes para el dropdown
    clientes = Cliente.objects.all()
    return render(request, 'mascotas/agregar_mascotas.html', {'clientes': clientes})

def ver_mascotas(request):
    mascotas = Animal.objects.all().select_related('dueno')  # Optimiza la consulta del dueño
    return render(request, 'mascotas/ver_mascotas.html', {'mascotas': mascotas})

def ver_detalle_mascota(request, id_animales):
    mascota = get_object_or_404(Animal, id_animales=id_animales)
    return render(request, 'mascotas/detalle_mascota.html', {'mascota': mascota})

def actualizar_mascota(request, id_animales):
    mascota = get_object_or_404(Animal, id_animales=id_animales)
    clientes = Cliente.objects.all()  # Obtener lista de clientes
    return render(request, 'mascotas/actualizar_mascotas.html', {
        'mascota': mascota,
        'clientes': clientes
    })

def realizar_actualizacion_mascota(request, id_animales):
    if request.method == 'POST':
        mascota = get_object_or_404(Animal, id_animales=id_animales)
        mascota.nombre = request.POST['nombre']
        mascota.edad = request.POST['edad']
        mascota.peso = request.POST['peso']
        mascota.cuidados = request.POST['cuidados']
        mascota.enfermedades = request.POST['enfermedades']
        mascota.especie = request.POST['especie']
        mascota.alimentacion = request.POST['alimentacion']
        
        # Manejar la asignación del dueño
        dueno_id = request.POST.get('dueno')
        if dueno_id:
            try:
                dueno = Cliente.objects.get(id_cliente=dueno_id)
                mascota.dueno = dueno
            except Cliente.DoesNotExist:
                mascota.dueno = None  # Si no existe, quitar dueño
        else:
            mascota.dueno = None  # Si no se selecciona dueño
        
        # Manejar la imagen si se proporciona una nueva
        if 'imagen' in request.FILES:
            mascota.imagen = request.FILES['imagen']
            
        mascota.save()
        return redirect('ver_mascotas')

    return redirect('ver_mascotas')

def borrar_mascota(request, id_animales):
    mascota = get_object_or_404(Animal, id_animales=id_animales)

    if request.method == 'POST':
        mascota.delete()
        return redirect('ver_mascotas')

    return render(request, 'mascotas/borrar_mascotas.html', {'mascota': mascota})


def inicio_clientes(request):
    return render(request, 'clientes/inicio_clientes.html')

def agregar_cliente(request):
    if request.method == 'POST':
        # Crear nuevo cliente con datos del formulario
        nuevo_cliente = Cliente(
            nombre=request.POST['nombre'],
            apepaterno=request.POST['apepaterno'],
            apematerno=request.POST['apematerno'],
            domicilio=request.POST['domicilio'],
            correo=request.POST['correo'],
            telefono=request.POST['telefono'],
            alergias=request.POST['alergias']
        )
        nuevo_cliente.save()
        return redirect('ver_clientes')
    
    return render(request, 'clientes/agregar_clientes.html')

def ver_clientes(request):
    clientes = Cliente.objects.all().prefetch_related('animales_poseidos')  # Optimiza la consulta de mascotas
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def ver_detalle_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})

def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'clientes/actualizar_clientes.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id_cliente):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
        cliente.nombre = request.POST['nombre']
        cliente.apepaterno = request.POST['apepaterno']
        cliente.apematerno = request.POST['apematerno']
        cliente.domicilio = request.POST['domicilio']
        cliente.correo = request.POST['correo']
        cliente.telefono = request.POST['telefono']
        cliente.alergias = request.POST['alergias']
        cliente.save()
        return redirect('ver_clientes')
    
    return redirect('ver_clientes')

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    
    return render(request, 'clientes/borrar_clientes.html', {'cliente': cliente})

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
        
        # Asignar mascotas a cargo si se seleccionaron
        mascotas_ids = request.POST.getlist('mascotas')
        if mascotas_ids:
            mascotas = Animal.objects.filter(id_animales__in=mascotas_ids)
            nuevo_empleado.animales_a_cargo.set(mascotas)
        
        return redirect('ver_empleados')
    
    # Obtener lista de mascotas para el dropdown
    mascotas = Animal.objects.all().select_related('dueno')
    return render(request, 'empleados/agregar_empleados.html', {'mascotas': mascotas})

def ver_empleados(request):
    empleados = Empleado.objects.all().prefetch_related('animales_a_cargo')  # Optimiza la consulta de mascotas
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    mascotas = Animal.objects.all().select_related('dueno')  # Obtener lista de mascotas
    return render(request, 'empleados/actualizar_empleados.html', {
        'empleado': empleado,
        'mascotas': mascotas
    })

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
        
        # Actualizar mascotas a cargo
        mascotas_ids = request.POST.getlist('mascotas')
        mascotas = Animal.objects.filter(id_animales__in=mascotas_ids)
        empleado.animales_a_cargo.set(mascotas)
        
        return redirect('ver_empleados')
    
    return redirect('ver_empleados')

def borrar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    
    return render(request, 'empleados/borrar_empleados.html', {'empleado': empleado})