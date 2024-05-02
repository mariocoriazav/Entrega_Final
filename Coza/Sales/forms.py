from django import forms

from .models import Venta, Serie


class VentaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de usuario"
    )


class VentaCreateForm(forms.Form):
    pass


class CodigoCreateForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ["nombre", "disponible", "capacidad"]
        widgets = {
            'capacidad': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Capacidad máxima de personas'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la sala'}),
            # 'disponible' does not need a custom widget for a simple checkbox.
        }
        labels = {
            "nombre": "Elegir un nombre para la Sala",
            "disponible": "Disponible",
            "capacidad": "Capacidad máxima",
        }


# class ReservaSearchForm(forms.Form):
#     nombre_de_usuario = forms.CharField(max_length=50, required=False, label="Nombre de Usuario")
#     sala = forms.ModelChoiceField(queryset=Sala.objects.all(), required=False, label="Sala")

#     def __init__(self, *args, **kwargs):
#         super(ReservaSearchForm, self).__init__(*args, **kwargs)
#         self.fields['sala'].queryset = Sala.objects.filter(disponible=True) if self.data.get('disponible') else Sala.objects.all()


class ReservaCreateForm(forms.ModelForm):
    class Meta:
        model = Reserva
        # Specifying which fields should appear in the form, including 'sala'
        fields = [
            "nombre_de_usuario",
            "sala",
            "fecha",
            "hora_inicio",
            "hora_fin",
            "descripcion",
        ]
        widgets = {
            "fecha": forms.DateInput(
                attrs={"type": "date"}
            ),  # Use HTML5 date picker for the 'fecha' field
            "hora_inicio": forms.TimeInput(
                attrs={"type": "time"}
            ),  # Use HTML5 time input for 'hora_inicio'
            "hora_fin": forms.TimeInput(
                attrs={"type": "time"}
            ),  # Use HTML5 time input for 'hora_fin'
            "descripcion": forms.Textarea(
                attrs={"rows": 3}
            ),  # Provide a larger text area for 'descripcion'
        }

    def __init__(self, *args, **kwargs):
        super(ReservaCreateForm, self).__init__(*args, **kwargs)
        # Optionally, you can further customize the 'sala' field here, for example:
        self.fields["sala"].queryset = Sala.objects.filter(
            disponible=True
        )  # Limit choices to available rooms
        self.fields["sala"].label = "Sala"  # Customize the field label
        # Any other field customizations can be done here