from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Mascota, SolicitudAdopcion, PublicacionBlog
from .forms import (
    SolicitudAdopcionForm,
    CustomUserCreationForm,
    MascotaForm,
    FotoMascotaFormSet,
    PublicacionBlogForm,
)
from django.contrib.admin.views.decorators import staff_member_required

# ==============================
# Mascotas
# ==============================


def listar_mascotas(request):
    """
    Lista todas las mascotas disponibles para adopción.
    """
    mascotas = Mascota.objects.filter(disponible=True)

    # Obtener parámetros de la URL
    especie = request.GET.get("especie")
    sexo = request.GET.get("sexo")
    tamaño = request.GET.get("tamaño")
    ubicacion = request.GET.get("ubicacion")

    if especie and especie != "":
        mascotas = mascotas.filter(especie__icontains=especie)
    if sexo and sexo != "":
        mascotas = mascotas.filter(sexo=sexo)
    if tamaño and tamaño != "":
        mascotas = mascotas.filter(tamaño=tamaño)
    if ubicacion and ubicacion != "":
        mascotas = mascotas.filter(ubicacion__icontains=ubicacion)

    return render(
        request,
        "mascotas/listar_mascotas.html",
        {
            "mascotas": mascotas,
            "valores": {
                "especie": especie or "",
                "sexo": sexo or "",
                "tamaño": tamaño or "",
                "ubicacion": ubicacion or "",
            },
        },
    )


def registrar_mascota(request):
    """
    Registrar una nueva mascota
    """
    if request.method == "POST":
        form = MascotaForm(request.POST)
        formset = FotoMascotaFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            mascota = form.save()
            fotos = formset.save(commit=False)
            for foto in fotos:
                foto.mascota = mascota
                foto.save()
            return redirect("listar_mascotas")
    else:
        form = MascotaForm()
        formset = FotoMascotaFormSet()

    return render(
        request,
        "mascotas/registrar_mascota.html",
        {
            "form": form,
            "formset": formset,
        },
    )


def detalle_mascota(request, pk):
    """
    Mostrar en detalle una mascota
    """
    mascota = get_object_or_404(Mascota, pk=pk)
    fotos = mascota.fotos.all()  # accede a las fotos relacionadas
    return render(
        request,
        "mascotas/detalle_mascota.html",
        {
            "mascota": mascota,
            "fotos": fotos,
        },
    )


@user_passes_test(lambda u: u.is_staff)
def editar_mascota(request, pk):
    """
    Edita los datos de una mascota registrada
    """
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        form = MascotaForm(request.POST, instance=mascota)
        formset = FotoMascotaFormSet(request.POST, request.FILES, instance=mascota)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "La mascota fue actualizada correctamente.")
            return redirect("detalle_mascota", pk=mascota.pk)
    else:
        form = MascotaForm(instance=mascota)
        formset = FotoMascotaFormSet(instance=mascota)

    return render(
        request,
        "mascotas/editar_mascota.html",
        {
            "form": form,
            "formset": formset,
            "mascota": mascota,
        },
    )


@user_passes_test(lambda u: u.is_staff)
def eliminar_mascota(request, pk):
    """
    Elimina una mascota registrada
    """
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        mascota.delete()
        messages.success(request, "La mascota fue eliminada correctamente.")
        return redirect("listar_mascotas")

    return render(request, "mascotas/eliminar_mascota.html", {"mascota": mascota})


# ==============================
# Solicitudes de adopción
# ==============================


@login_required
def solicitar_adopcion(request, mascota_id):
    """
    Permite a un usuario solicitar la adopción de una mascota.
    """
    mascota = get_object_or_404(Mascota, id=mascota_id)

    if request.method == "POST":
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.mascota = mascota
            solicitud.save()
            messages.success(request, "Tu solicitud de adopción ha sido enviada.")
            return redirect("listar_mascotas")
    else:
        form = SolicitudAdopcionForm()

    return render(
        request, "mascotas/solicitar_adopcion.html", {"form": form, "mascota": mascota}
    )


@user_passes_test(lambda u: u.is_staff)  # solo staff/admin puede ver
def listar_solicitudes(request):
    """
    Muestra todas las solicitudes de adopción (solo staff).
    """
    solicitudes = SolicitudAdopcion.objects.all().order_by("-fecha_solicitud")
    return render(
        request, "mascotas/listar_solicitudes.html", {"solicitudes": solicitudes}
    )


@staff_member_required
def aprobar_solicitud(request, solicitud_id):
    """
    Marca una solicitud como aprobada (solo staff).
    """
    solicitud = get_object_or_404(SolicitudAdopcion, id=solicitud_id)
    solicitud.estado = "aprobada"
    solicitud.save()

    solicitud.mascota.disponible = False
    solicitud.mascota.save()

    messages.success(request, f"Solicitud de {solicitud.usuario.username} aprobada ✅")
    return redirect("listar_solicitudes")


@staff_member_required
def rechazar_solicitud(request, solicitud_id):
    """
    Marca una solicitud como rechazada (solo staff).
    """
    solicitud = get_object_or_404(SolicitudAdopcion, id=solicitud_id)
    solicitud.estado = "rechazada"
    solicitud.save()
    messages.error(request, f"Solicitud de {solicitud.usuario.username} rechazada ❌")
    return redirect("listar_solicitudes")


# ==============================
# Publicaciones Blog
# ==============================


def listar_publicaciones(request):
    """
    Lista todas las publicaciones del blog.
    """
    publicaciones = PublicacionBlog.objects.all().order_by("-fecha_publicacion")
    return render(
        request, "mascotas/listar_publicaciones.html", {"publicaciones": publicaciones}
    )



def detalle_publicacion(request, pk):
    """
    Muestra en detalle una publicacion en el sistema
    """
    post = get_object_or_404(PublicacionBlog, pk=pk)
    return render(request, "mascotas/detalle_publicacion.html", {"post": post})


@user_passes_test(lambda u: u.is_staff)
def crear_publicacion(request):
    """
    Crea una publicacion para un usuario staff
    """
    if request.method == "POST":
        form = PublicacionBlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  # usa el CustomUser autenticado (staff)
            post.save()
            messages.success(request, "Publicación creada correctamente.")
            return redirect("detalle_publicacion", pk=post.pk)
    else:
        form = PublicacionBlogForm()
    return render(request, "mascotas/crear_publicacion.html", {"form": form})



@login_required
@user_passes_test(lambda u: u.is_staff)
def editar_publicacion(request, pk):
    """
    Edita una publicacion para un usuario staff
    """
    post = get_object_or_404(PublicacionBlog, pk=pk)
    if request.method == "POST":
        form = PublicacionBlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Publicación actualizada correctamente.")
            return redirect("detalle_publicacion", pk=post.pk)
    else:
        form = PublicacionBlogForm(instance=post)
    return render(
        request, "mascotas/editar_publicacion.html", {"form": form, "post": post}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def eliminar_publicacion(request, pk):
    """
    Elimina una publicacion para un usuario staff
    """
    post = get_object_or_404(PublicacionBlog, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Publicación eliminada.")
        return redirect("listar_publicaciones")
    return render(request, "mascotas/eliminar_publicacion.html", {"post": post})


# ==============================
# Registro de usuarios
# ==============================


def registro_usuario(request):
    """
    Permite a un nuevo usuario registrarse en el sistema.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Tu cuenta ha sido creada con éxito. Ahora puedes iniciar sesión.",
            )
            return redirect("login")  # requiere urls de auth
    else:
        form = CustomUserCreationForm()

    return render(request, "mascotas/registro_usuario.html", {"form": form})
