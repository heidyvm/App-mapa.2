from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render 

def damefecha(request):
    fecha_actual=datetime.datetime.now()
    documento= """<html>
     <body>
    <h2>Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" %fecha_actual
    return HttpResponse(documento)

def pantprincipal(request):
    #ahora=datetime.datetime.now()
    #return render(request, "indexprincipal.html", {"momento_actual":ahora})
    fecha_actual=datetime.datetime.now()
    return render (request, "indexprincipal.html", {"damefecha":fecha_actual})

def acceso(request):
    fecha_actual=datetime.datetime.now()
    return render (request, "acceder-cuenta.html"), {"damefecha":fecha_actual}

def registro(request):
    fecha_actual=datetime.datetime.now()
    return render (request, "registrar-cuenta.html", {"damefecha":fecha_actual})

def olvidocontr(request):
    fecha_actual=datetime.datetime.now()
    return render (request, "olvido-de-contraseña.html", {"damefecha":fecha_actual})


