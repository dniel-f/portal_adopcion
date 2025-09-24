# Portal Adopción

## Descripción
Portal web para la gestión de adopción de mascotas, incluyendo funcionalidades de registro de usuarios, publicación de mascotas, solicitudes de adopción y un blog. El proyecto está desarrollado con **Django 5** y utiliza **SQLite** como base de datos por defecto.

---

## Tecnologías utilizadas
- **Backend:** Django 5.2.6, Python 3.12  
- **Base de datos:** SQLite3  
- **Gestión de imágenes:** Pillow  
- **Control de versiones:** Git  
- **Plantillas:** Django Templates (HTML)

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/dniel-f.git
cd portal-adopcion
```
2. Crear un entorno virtual y activarlo:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt

```


4. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Correr el servidor:
```bash
python manage.py runserver
```
Abrir en el navegador: http://127.0.0.1:8000/

---

## Estructura del proyecto
portal_adopcion/
├── db.sqlite3
├── manage.py
├── mascotas/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── portal_adopcion/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                 # Imágenes subidas
├── mascotas.ddl            # Definición de base de datos
├── requirements.txt
├── populate.py             # Script de datos de prueba
└── README.md

---

## Funcionalidades principales

**Usuarios:**

- Registro y gestión de usuarios con campos adicionales (teléfono, dirección).

- Gestión de permisos: solo staff/admin puede crear, editar o eliminar publicaciones del blog.

**Mascotas:**

- Registro de mascotas con información completa: especie, raza, edad, sexo, tamaño, estado de salud, descripción y ubicación.

- Subida de fotos de mascotas (varias por mascota).

**Solicitudes de adopción:**

- Los usuarios pueden enviar solicitudes de adopción para mascotas disponibles.

- Estado de solicitud: pendiente, aprobada, rechazada.

**Blog:**

- CRUD completo de publicaciones de blog (solo staff/admin).

- Visualización de publicaciones por cualquier usuario.

---

## Dependencias

- Django==5.2.6
- asgiref==3.9.1
- pillow==11.3.0
- sqlparse==0.5.3

---

## Notas adicionales

- Los archivos sensibles, el entorno virtual y las migraciones generadas están excluidos mediante .gitignore.
- Se recomienda usar venv para aislar dependencias y evitar conflictos.

## Autor
Daniel Figueroa
