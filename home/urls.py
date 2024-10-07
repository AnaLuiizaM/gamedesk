from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_page, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro', views.cadastro_view, name='cadastro'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]