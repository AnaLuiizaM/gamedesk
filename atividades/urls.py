from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('lista-de-atividades/', views.atividades_view, name='lista de atividades'),
    path('cadastro-de-atividades/', views.criar_atividade, name='cadastro de atividades'),
    ]