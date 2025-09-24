from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SolicitudAdopcion, CustomUser, Mascota, FotoMascota, PublicacionBlog
from django.forms import inlineformset_factory


class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ["mensaje"]  # solo mensaje, usuario y mascota se asignan en la vista


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "edad", "sexo", "tamaño", "estado_salud", "descripcion", "ubicacion", "disponible"]

class FotoMascotaForm(forms.ModelForm):
    class Meta:
        model = FotoMascota
        fields = ["imagen", "descripcion"]

# Formset para asociar varias fotos a una mascota
FotoMascotaFormSet = inlineformset_factory(
    Mascota, FotoMascota, form=FotoMascotaForm,
    extra=3, can_delete=True
)


class PublicacionBlogForm(forms.ModelForm):
    class Meta:
        model = PublicacionBlog
        fields = ("titulo", "contenido")
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título"}),
            "contenido": forms.Textarea(attrs={"class": "form-control", "rows": 8, "placeholder": "Contenido..."}),
        }