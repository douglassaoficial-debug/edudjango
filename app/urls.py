from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('status/', views.status_view, name='status'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
]
