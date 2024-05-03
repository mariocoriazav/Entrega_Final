from django import forms

from .models import Venta, Serie


class VentaSearchForm(forms.Form):
    nombre_usuario = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de usuario"
    )

class CodigoSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de código"
    )



class CodigoCreateForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["nombre", "disponible", "capacidad"]
        widgets = {
            'capacidad': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Capacidad máxima de productos'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del código'}),
            # 'disponible' does not need a custom widget for a simple checkbox.
        }
        labels = {
            "nombre": "Elegir un nombre para el Código",
            "disponible": "Disponible",
            "capacidad": "Capacidad máxima",
        }

