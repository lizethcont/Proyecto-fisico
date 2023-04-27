from django.db import models


class Persona(models.Model):
    unidad = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    grado = models.CharField(max_length=100)  
    certificacion = models.CharField(max_length=100)
    test = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10)
    numerocelu = models.CharField(max_length=10)
    correo = models.EmailField()
    edad = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    genero = models.CharField(max_length=1)
    flexiones = models.IntegerField()
    abdominales = models.IntegerField()
    prueba_aerobica = models.CharField(max_length=5)
    imc = models.FloatField()  
    estado = models.CharField(max_length=100) 
    estado_p = models.CharField(max_length=100)
    metabolismo_basal = models.FloatField()  
    calificacion_total = models.FloatField()  