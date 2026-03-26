from django.urls import path
from . import views

urlpatterns = [
    # caminho, view, apelido
    path('', views.dashboard, name='dashboard'),
    path('clientes/', views.clientes, name='clientes'),
    path('emitir/', views.emitir_nota, name='emitir_nota'),
]