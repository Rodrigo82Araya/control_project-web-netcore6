from dataclasses import field
from msilib.schema import CheckBox
from tkinter import Widget
from django import forms
from .models import Orden, Seguimiento
from django.forms import  TextInput, Textarea

class OrdenesForm(forms.ModelForm):
    
    class Meta:
        model = Orden
        fields = ['nombre','descripcion','prioridad']
        widgets = {
            'descripcion': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Ingrese el detalle de la orden'
            }),            
        }

    def __init__(self, *args, **kwargs):
        super(OrdenesForm, self).__init__(*args,**kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Ingrese el nombre de la orden'
        self.fields['prioridad'].widget.attrs['class'] = 'form-check-input'        

        for field in self.fields:
            if field != 'prioridad':
                self.fields[field].widget.attrs['class']='form-control'
        
class SeguimientoForm(forms.ModelForm):
    
    class Meta:
        model = Seguimiento
        fields = ['id_orden', 'id_usuario_asignado','nombre','status','cant_dias_proy']
        widgets = {"id_orden": forms.TextInput(),"id_orden": forms.HiddenInput()}
        
    def __init__(self, *args, **kwargs):
        super(SeguimientoForm, self).__init__(*args,**kwargs)   

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'