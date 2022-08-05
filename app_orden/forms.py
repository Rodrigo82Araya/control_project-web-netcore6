from dataclasses import field
from tkinter import Widget
from django import forms
from .models import Orden
from django.forms import  TextInput, Textarea

class OrdenesForm(forms.ModelForm):
    

    class Meta:        
        model = Orden
        fields = ['nombre','descripcion']
        widgets = {
            'nombre': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Ingrese el nombre de la orden'
                }),
            'descripcion': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Ingrese el detalle de la orden'
                })
        }
        