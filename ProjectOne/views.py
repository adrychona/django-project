from django.http import HttpResponse
from django.template import Template, Context, loader
#from django.views import render 
import datetime as dt
import random 

def bienvenida(request):
    return HttpResponse("Hola, bienvenidos a mi segunda página web :')")

def solicitudes(request):
    return HttpResponse("Por favor, haga su solicitud")

def hora_actual(request):
    ahora = dt.datetime.now()
    mensaje = f"la hora actual es {ahora.hour}:{ahora.minute}:{ahora.second}"
    return HttpResponse(mensaje)

def saludar(request, nombre):
    mensaje = f'Hola {nombre}. Mucho gusto!'
    return HttpResponse(mensaje)

def inicio(nombre):
    #Forma 1
    #f= open(r"/Users/adrychona/Desktop/ProyectoDjango/ProjectOne/ProjectOne/Templates/inicio.html") #use r (row) to ignore /n.. In windows slash are the other way and they need to be /.
    #plantilla = Template(f.read())
    #f.close()
    #alearorio = random.randint(1,100)
    #info = {"numero":alearorio }
    #context = Context(info)
    #plantilla = plantilla.render(context)    #pasando la info del diccionatio al HTML
    #context = Context({"numero":alearorio})


    #Forma 2 
    # url fue agregado en settings.py
    plantilla = loader.get_template("inicio.html")
    aleatorio = random.randint(1,10)
    info = {"numero":aleatorio}
    plantilla = plantilla.render(info)

    return HttpResponse(plantilla) #needs to be rendered to work

