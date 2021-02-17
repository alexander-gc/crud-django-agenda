from django.shortcuts import render, redirect
from apps.agenda.models import Agenda

# Create your views here.
def index_agenda(request):
    agenda_lista = Agenda.objects.all()
    return render(request, "agenda/index.html", context={"agenda_lista": agenda_lista})

def crear_agenda(request):
    if request.method == "POST":
        numero = request.POST["numero"]
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        Agenda.objects.create(numero=numero, nombre=nombre, descripcion=descripcion)
    return render(request, "agenda/create.html")

def editar_agenda(request, id):
    tarea = Agenda.objects.get(id=id)

    if request.method == "POST":

        numero = request.POST["numero"]
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]

        tarea.numero = numero
        tarea.nombre = nombre
        tarea.descripcion = descripcion

        tarea.save()
    return render(request, "agenda/create.html", {"tarea": tarea})

def borrar_agenda(request, id):
    Agenda.objects.get(id=id).delete()
    return redirect("index")