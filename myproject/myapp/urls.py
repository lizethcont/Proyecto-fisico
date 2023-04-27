from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('calcular-imc/', views.calcular_imc_view, name='calcular_imc'),
    path('imc_por_edad/', views.imc_por_edad, name='imc-por-edad'),
    path('success/', views.success_view, name='success'),
]