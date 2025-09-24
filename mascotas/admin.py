# mascotas/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Mascota, SolicitudAdopcion, PublicacionBlog, FotoMascota

# -----------------------------
# CustomUser admin
# -----------------------------
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('telefono','direccion')}),
    )
    list_display = ('username', 'email', 'is_staff', 'telefono', 'direccion')
    search_fields = ('username', 'email', 'telefono')
    ordering = ('username',)


# -----------------------------
# FotoMascota Inline
# -----------------------------
class FotoMascotaInline(admin.TabularInline):
    model = FotoMascota
    extra = 1  # formularios extra vacíos


# -----------------------------
# Mascota admin
# -----------------------------
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'edad', 'sexo', 'disponible', 'ubicacion', 'fecha_registro')
    list_filter = ('especie', 'sexo', 'disponible', 'ubicacion', 'fecha_registro')
    search_fields = ('nombre', 'raza', 'ubicacion')
    ordering = ('-fecha_registro',)
    inlines = [FotoMascotaInline]


# -----------------------------
# SolicitudAdopcion admin
# -----------------------------
@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mascota', 'estado', 'fecha_solicitud')
    list_filter = ('estado', 'fecha_solicitud')
    search_fields = ('usuario__username','mascota__nombre')
    ordering = ('-fecha_solicitud',)


# -----------------------------
# PublicacionBlog admin
# -----------------------------
@admin.register(PublicacionBlog)
class PublicacionBlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    list_filter = ('fecha_publicacion','autor')
    search_fields = ('titulo','autor__username')
    ordering = ('-fecha_publicacion',)
