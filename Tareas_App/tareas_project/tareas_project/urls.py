"""tareas_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestor_tareas.views import inicio,add_task,delete_task,edit_task,save_edit_task,entrar,verificar_usuario,registrar_usuario,agregar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",entrar),
    path("registrar/",registrar_usuario),
    path("validar_registro/",agregar_usuario),
    path("verificar_usuario/",verificar_usuario),
    path("foro/",inicio),
    path("Subir/",add_task),
    path("delete/<int:id>/",delete_task),
    path("editar/<int:id>",edit_task),
    path("save/edit/<int:id>",save_edit_task)
]
