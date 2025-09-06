from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('noticias/', views.noticias, name='noticias'),
    path('herramientas/', views.herramientas, name='herramientas'),
    path('nosotros/', views.nosotros, name='nosotros')
]
