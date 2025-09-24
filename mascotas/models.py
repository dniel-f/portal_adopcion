# mascotas/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


# -----------------------------
# Custom User
# -----------------------------
class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.username

# -----------------------------
# Mascota
# -----------------------------
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10, choices=[('Macho','Macho'),('Hembra','Hembra')])
    tamaño = models.CharField(max_length=20, choices=[('Pequeño','Pequeño'),('Mediano','Mediano'),('Grande','Grande')])
    estado_salud = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"


class FotoMascota(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="fotos")
    imagen = models.ImageField(upload_to="mascotas/fotos/")
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Foto de {self.mascota.nombre}"

# -----------------------------
# Solicitud de Adopción
# -----------------------------
class SolicitudAdopcion(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada')
    ], default='pendiente')
    mensaje = models.TextField(blank=True, null=True)  # 👈 Agregado

    def __str__(self):
        return f"{self.usuario.username} - {self.mascota.nombre}"


# -----------------------------
# Blog
# -----------------------------
class PublicacionBlog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

