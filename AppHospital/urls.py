from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppHospital/inicio.html'), name='logout'),
    path('editarPerfil/', editarPerfil , name='editarPerfil'),
    path('', inicio, name='inicio'),
    path('sobreMi/', sobreMi ,name='sobreMi'),
    path('agregarAvatar/',agregarAvatar  ,name='agregarAvatar'),
    path('comentarios/', comentarios ,name='comentarios'),
    path('publicaciones/', publicaciones  ,name='publicaciones'),
    path('leerPublicaciones/', leerPublicaciones , name='leerPublicacion' ),
    path('eliminarPublicacion/<publicacion_publicacion>/', eliminarPublicacion , name='eliminarPublicacion' ),
    path('editarPublicacion/<publicacion_publicacion>/', editarPublicacion , name='editarPublicacion' ),    
]