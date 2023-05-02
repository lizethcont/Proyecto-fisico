from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    genero = forms.ChoiceField(choices=[('S', 'Seleccione una opcion'), ('F', 'Femenino'), ('M', 'Masculino')])
    unidad = forms.ChoiceField(choices=[('S', 'Seleccione una opcion'),('Cmd', 'Comando'), ('JEM', 'JEM'), ('IG - FF.AA.', 'IG - FF.AA.'), ('DEPTO I', 'DEPTO I'), ('DEPTO II', 'DEPTO II'), ('DEPTO III', 'DEPTO III'), ('DEPTO IV', 'DEPTO IV'), 
                                        ('DEPTO V', 'DEPTO V'), ('DEPTO VI', 'DEPTO VI'), ('DEPTO VII', 'DEPTO VII'), ('DEPTO VIII', 'DEPTO VIII'), ('DEPTO IX', 'DEPTO IX'), ('DAF', 'DAF'), ('DICOS', 'DICOS'),
                                        ('DIGEPLAE', 'DIGEPLAE'), ('DIR - BIE - PATRIMONIO', 'DIR - BIE - PATRIMONIO'), ('EAEN', 'EAEN'), ('ABHM', 'ABHM'), ('DIGEARCH', 'DIGEARCH'), ('UNIVERSIDAD MILITAR', 'UNIVERSIDAD MILITAR'), ('OTROS', 'OTROS')])
    certificacion = forms.ChoiceField(choices=[('S', 'Seleccione una opcion'), ('No Apto', 'No Apto'), ('Apto', 'Apto')])
    test = forms.ChoiceField(choices=[('S', 'Seleccione una opcion'),('Positivo', 'Positivo'), ('Negativo', 'Negativo'), ('No Corresponde', 'No Corresponde')])

    class Meta:
        model = Persona
        fields = ['unidad','nombre', 'grado', 'certificacion', 'test', 'cedula', 'numerocelu', 'correo', 'edad', 'peso', 'altura', 'genero', 'abdominales', 'flexiones','prueba_aerobica']