from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada', 'hora']
        widgets = {
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }