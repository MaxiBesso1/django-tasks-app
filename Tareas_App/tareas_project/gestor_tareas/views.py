from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context
from gestor_tareas.models import Tarea
from gestor_tareas.models import Usuario

datos_usuario = {"nombre":"","id":0}
estado_secion = False
def entrar(request):
    return render(request,"entrar.html")

def verificar_usuario(request):
    global estado_secion
    global datos_usuario
    nombre_usuario = request.POST["username"]
    password_form = request.POST["password"]
    usuarios = Usuario.objects.all()
    print(usuarios)
    datos_usuario = {"nombre":"","id":0}

    #Proceso de verificacion de un usuario
    for user in usuarios:
        if user.nombre == nombre_usuario:
            if user.password == password_form:
                datos_extraidos = Usuario.objects.filter(nombre=nombre_usuario)
                for x in datos_extraidos:
                    id_usuario = x.id
                estado_secion = True
                datos_usuario = {"nombre":nombre_usuario,"id":id_usuario}
                print(datos_usuario)
    
    if estado_secion == False:
        return HttpResponseRedirect("/")
        
    
    return HttpResponseRedirect("/foro/")

def registrar_usuario(request):
    return render(request,"registrar.html")

def agregar_usuario(request):
    nombre_usuario = request.POST["username"]
    password = request.POST["password"]

    validacion = True

    user = ""

    nombres_usuarios = Usuario.objects.all()
    if user in nombres_usuarios:
        if user.nombre == nombre_usuario:
            validacion = False


    if validacion:
        Usuario.objects.create(nombre=nombre_usuario,password=password)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("registrarse/")


# Create your views here.

def inicio(request):
    global datos_usuario
    if estado_secion:
        query=Tarea.objects.filter(creador=datos_usuario["nombre"])
        return render(request,"index.html",{"tasks":query})
    else:
        return HttpResponseRedirect("/")

def add_task(request):

    task_name= request.GET["task-name"]
    task_description = request.GET["task-description"]
    task_priority = request.GET["task-priority"]
    task_creator = datos_usuario["nombre"]

    if task_name != "" and task_description!="" and task_priority!="":
        Tarea.objects.create(nombre=task_name,descripcion=task_description,prioridad=task_priority,creador=task_creator)
        return HttpResponseRedirect("/foro")
    else:
        return HttpResponse("Completa todos los campos!!!!")

def delete_task(request,id):
    task = Tarea.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect("/foro")

def edit_task(request,id):
    task = Tarea.objects.get(id=id)

    return render(request,"edit_task.html",{"task":task})

def save_edit_task(request,id):
    task = Tarea.objects.get(id=id)
    task.nombre = request.GET["task-name"]
    task.save()
    task.descripcion= request.GET["task-description"]
    task.save()
    task.prioridad=request.GET["task-priority"]
    task.save()
    return HttpResponseRedirect("/foro")


