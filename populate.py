import os
import django
import random
from django.utils import timezone

# Configurar entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_adopcion.settings')
django.setup()

from mascotas.models import CustomUser, Mascota, PublicacionBlog, SolicitudAdopcion

def populate():

    # 1. Crear usuarios
    if not CustomUser.objects.exists():
        usuarios = []
        for i in range(5):
            user = CustomUser.objects.create_user(
                username=f'user{i+1}',
                email=f'user{i+1}@mail.com',
                password='password123',
                telefono=f'+5691234567{i}',
                direccion=f'Calle Falsa {i+10}, Santiago'
            )
            usuarios.append(user)
        print("Usuarios creados.")
    else:
        usuarios = list(CustomUser.objects.all())
        print("Usuarios ya existen.")

    # 2. Crear mascotas
    if not Mascota.objects.exists():
        especies = ["Perro", "Gato", "Conejo", "Ave"]
        ubicaciones = ["Santiago", "Valparaíso", "Concepción", "La Serena"]
        for i in range(20):
            Mascota.objects.create(
                nombre=f'Mascota{i+1}',
                especie=random.choice(especies),
                edad=random.randint(1, 12),
                ubicacion=random.choice(ubicaciones),
                descripcion=f'Descripción de la mascota {i+1}'
            )
        print("Mascotas creadas.")
    else:
        print("Mascotas ya existen.")

    # 3. Crear publicaciones de blog
    if not PublicacionBlog.objects.exists():
        for i in range(10):
            PublicacionBlog.objects.create(
                titulo=f'Consejo {i+1}',
                contenido=f'Contenido de prueba para el consejo {i+1}.',
                fecha_publicacion=timezone.now(),
                autor=random.choice(usuarios)
            )
        print("Publicaciones creadas.")
    else:
        print("Publicaciones ya existen.")

    # 4. Crear solicitudes de adopción
    if not SolicitudAdopcion.objects.exists():
        mascotas = list(Mascota.objects.all())
        for i in range(5):
            SolicitudAdopcion.objects.create(
                usuario=random.choice(usuarios),
                mascota=random.choice(mascotas),
                fecha_solicitud=timezone.now(),
                estado=random.choice(['Pendiente', 'Aprobada', 'Rechazada'])
            )
        print("Solicitudes creadas.")
    else:
        print("Solicitudes ya existen.")

if __name__ == '__main__':
    populate()

