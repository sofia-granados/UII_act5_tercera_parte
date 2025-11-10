from django.db import models

# ==========================================
# MODELO: CLIENTES (debe definirse PRIMERO)
# ==========================================
class Cliente(models.Model):
    # Clave primaria
    id_cliente = models.AutoField(primary_key=True)
    apepaterno = models.CharField(max_length=100)
    apematerno = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20)
    alergias = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apepaterno}"

# ==========================================
# MODELO: EMPLEADOS 
# ==========================================
class Empleado(models.Model):
    # Clave primaria
    id_empleado = models.AutoField(primary_key=True)
    # Atributos personales
    apepaterno = models.CharField(max_length=100)
    apematerno = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    domicilio = models.TextField(blank=True, null=True)
    ocupacion = models.CharField(max_length=100)
    alergias = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Empleado: {self.nombre} {self.apepaterno} ({self.ocupacion})"

# ==========================================
# MODELO: ANIMALES (debe definirse DESPUÉS de Cliente)
# ==========================================
class Animal(models.Model):
    id_animales = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=20, blank=True, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    cuidados = models.TextField(blank=True, null=True)
    enfermedades = models.TextField(blank=True, null=True)
    especie = models.CharField(max_length=50)
    alimentacion = models.TextField(blank=True, null=True)
    # NUEVO: Campo para la imagen
    imagen = models.ImageField(
        upload_to='mascotas/', 
        blank=True, 
        null=True,
        verbose_name='Imagen de la mascota'
    )
    
    # RELACIÓN CON CLIENTE (ForeignKey)
    dueno = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="animales_poseidos",
        blank=True,
        null=True  # Permite animales sin dueño registrado si es necesario
    )
    
    # RELACIÓN CON EMPLEADOS (ManyToManyField)
    empleados_responsables = models.ManyToManyField(
        Empleado,
        related_name="animales_a_cargo",
        blank=True
    )

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - ID: {self.id_animales}"