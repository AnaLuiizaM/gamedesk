from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_page, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]