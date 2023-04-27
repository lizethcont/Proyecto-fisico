from django.contrib import admin
from .models import Persona
# Register your models here.
class MyappConfig(admin.ModelAdmin):
    list_display = ('peso', 'altura', 'edad', 'correo', 'nombre')
    search_fields = ('nombre', 'correo', 'edad')
    list_filter = ('nombre', 'edad', 'correo')

admin.site.register(Persona, MyappConfig) 