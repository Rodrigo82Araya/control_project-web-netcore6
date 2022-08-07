from dataclasses import field
from msilib.schema import CheckBox
from tkinter import Widget
from django import forms
from .models import Orden
from django.forms import  TextInput, Textarea

class OrdenesForm(forms.ModelForm):
    

    class Meta:        
        model = Orden
        fields = ['nombre','descripcion','prioridad']
        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Ingrese el nombre de la orden'
            }),
            'descripcion': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Ingrese el detalle de la orden'
            }),
            'prioridad':forms.widgets.CheckboxInput(attrs={
                'class': "form-check-input"
            })
        }
        