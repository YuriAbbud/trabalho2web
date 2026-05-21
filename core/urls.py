from django.urls import path
from . import views

urlpatterns = [
    # auth
    path('registro/', views.registro,     name='registro'),
    path('login/',    views.login_view,   name='login'),
    path('logout/',   views.logout_view,  name='logout'),
    # páginas
    path('',                views.dashboard,   name='dashboard'),
    path('clientes/',       views.clientes,    name='clientes'),
    # CRUD notas
    path('notas/',              views.lista_notas,  name='lista_notas'),
    path('emitir/',             views.emitir_nota,  name='emitir_nota'),
    path('notas/<int:pk>/',     views.detalhe_nota, name='detalhe_nota'),
    path('notas/<int:pk>/editar/',  views.editar_nota,  name='editar_nota'),
    path('notas/<int:pk>/deletar/', views.deletar_nota, name='deletar_nota'),
    path('clientes/novo/',              views.novo_cliente,    name='novo_cliente'),
    path('clientes/<int:pk>/editar/',   views.editar_cliente,  name='editar_cliente'),
    path('clientes/<int:pk>/deletar/',  views.deletar_cliente, name='deletar_cliente'),
]