from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atividades/', include('atividades.urls')),
    path('', include('home.urls')),
    path('equipe/', include('equipe.urls')),
]