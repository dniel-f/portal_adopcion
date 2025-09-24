from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SolicitudAdopcion, CustomUser, Mascota, FotoMascota, PublicacionBlog
from django.forms import inlineformset_factory


class SolicitudAdopcionForm(forms.ModelForm):
    """
    Formulario para crear una solicitud de adopción.
    Solo permite ingresar el mensaje, usuario y mascota se asignan en la vista.
    """
    class Meta:
        model = SolicitudAdopcion
        fields = ["mensaje"]


class CustomUserCreationForm(UserCreationForm):
    """
    Formulario para registrar un nuevo usuario personalizado (CustomUser).
    """
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")



class MascotaForm(forms.ModelForm):
    """
    Formulario para crear o editar una mascota.
    """
    class Meta:
        model = Mascota
        fields = [
            "nombre",
            "especie",
            "raza",
            "edad",
            "sexo",
            "tamaño",
            "estado_salud",
            "descripcion",
            "ubicacion",
            "disponible",
        ]


class FotoMascotaForm(forms.ModelForm):
    """
    Formulario para subir fotos de una mascota.
    """
    class Meta:
        model = FotoMascota
        fields = ["imagen", "descripcion"]


# Formset para asociar varias fotos a una mascota
FotoMascotaFormSet = inlineformset_factory(
    parent_model=Mascota,
    model=FotoMascota,
    form=FotoMascotaForm,
    extra=3,
    can_delete=True,
)


class PublicacionBlogForm(forms.ModelForm):
    """
    Formulario para crear o editar publicaciones de blog.
    """
    class Meta:
        model = PublicacionBlog
        fields = ("titulo", "contenido")
        widgets = {
            "titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Título"}
            ),
            "contenido": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Contenido...",
                }
            ),
        }