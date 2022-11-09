from django.http import HttpResponse
from appcoder.models import Curso
from django.shortcuts import render


def inicio(request):
    return render(request, "appcoder/index.html")


def cursos(request):
    # Obtenes el listado de objetos en la BD
    cursos = Curso.objects.all()

    for curso in cursos:
        print(curso.nombre)

    return render(request, "appcoder/cursos.html")


def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")


def profesores(request):
    return render(request, "appcoder/profesores.html")


def entregables(request):
    return render(request, "appcoder/entregables.html")
# Create your views here.
