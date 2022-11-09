from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader


def vista_saludo(request):
    return HttpResponse("<h1>Hola Coders! :)<h1>")


def iniciar_sesion(request):
    return HttpResponse("Ingresa tu usuario y contraseña!")


def dia_hoy(request, nombre):
    hoy = datetime.now()
    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)


def anio_nacimiento(request, edad):
    edad = int(edad)
    anio_nac = datetime.now().year - edad
    return HttpResponse(f"Naciste en {anio_nac} ")


def vista_plantilla(request):
    # abrimos el archivo
    archivo = open(
        r"C:\Users\User\Desktop\DJANGO\proyectocoder\proyectocoder\templates\plantilla_bonita.html")
# creamos el objeto "plantilla"
    plantilla = Template(archivo.read())
    # cerramos el archivo para liberar recursos
    archivo.close()
# diccionario con datos para la plantilla
    datos = {"nombre": "Facundo", "fecha": datetime.now(), "apellido": "Olmos"}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def vista_listado_alumnos(request):

    archivo = open(
        r"C:\Users\User\Desktop\DJANGO\proyectocoder\proyectocoder\templates\listado_alumnos.html")
    plantilla = Template(archivo.read())
    archivo.close()
    listado_alumnos = ["leonel gareis", "agustin russo", "cristian garcia",
                       "angelo pettinari", "diego ibarra", "santiago ortiz", "barbara vivante", "barbara pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}
    contexto = Context(datos)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def vista_listado_alumnos2(request):
    listado_alumnos = ["leonel gareis", "agustin russo", "cristian garcia",
                       "angelo pettinari", "diego ibarra", "santiago ortiz", "barbara vivante", "barbara pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template(listado_alumnos.html)
    documento = plantilla.render(datos)

    return HttpResponse(documento)
