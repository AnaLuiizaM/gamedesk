from django.urls import path
from . import views

urlpatterns = [
    path('lista-de-equipe/', views.equipe_view, name='lista de equipe'),
    path('cadastro-de-equipe/', views.cadastro_view, name='cadastro de equipe'),
    ]