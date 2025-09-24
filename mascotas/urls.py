from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # -----------------------------
    # Mascotas
    # -----------------------------
    path("", views.listar_mascotas, name="listar_mascotas"),
    path("mascota/<int:pk>/editar/", views.editar_mascota, name="editar_mascota"),
    path("mascota/<int:pk>/eliminar/", views.eliminar_mascota, name="eliminar_mascota"),
    path("mascota/<int:pk>/", views.detalle_mascota, name="detalle_mascota"),
    path("registrar/", views.registrar_mascota, name="registrar_mascota"),
    # -----------------------------
    # Solicitudes de adopción
    # -----------------------------
    path(
        "adoptar/<int:mascota_id>/", views.solicitar_adopcion, name="solicitar_adopcion"
    ),
    path("solicitudes/", views.listar_solicitudes, name="listar_solicitudes"),
    path(
        "solicitudes/aprobar/<int:solicitud_id>/",
        views.aprobar_solicitud,
        name="aprobar_solicitud",
    ),
    path(
        "solicitudes/rechazar/<int:solicitud_id>/",
        views.rechazar_solicitud,
        name="rechazar_solicitud",
    ),
    # -----------------------------
    # Registro de usuarios
    # -----------------------------
    path("registro/", views.registro_usuario, name="registro_usuario"),
    # -----------------------------
    # Login / Logout (auth built-in)
    # -----------------------------
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="mascotas/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="listar_mascotas"), name="logout"),
    # -----------------------------
    # Publicaciones / Blog
    # -----------------------------
    path("blog/", views.listar_publicaciones, name="listar_publicaciones"),
    path("blog/<int:pk>/", views.detalle_publicacion, name="detalle_publicacion"),
    path("blog/crear/", views.crear_publicacion, name="crear_publicacion"),
    path("blog/<int:pk>/editar/", views.editar_publicacion, name="editar_publicacion"),
    path(
        "blog/<int:pk>/eliminar/",
        views.eliminar_publicacion,
        name="eliminar_publicacion",
    ),
]
