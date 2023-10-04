from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from Aplicacion1.models import Cliente, Proveedores, Productos

def inicio(request):
    return render(request,r"Aplicacion1\inicio.html")


def crear_cliente(request,nombre,razon_social):
    cliente = Cliente(nombre=nombre, razon_social=razon_social)
    cliente.save()
    return render(request,r"Aplicacion1\crear_usuario.html")

def alta_proveedor(request,proveedor,tipo):
    prov = Proveedores(proveedor=proveedor, tipo=tipo)
    prov.save()
    return render(request,r"Aplicacion1\crear_proveedor.html")

def prod(request,producto,subrubro,rubro):
    prod = Productos(producto=producto, subrubro=subrubro, rubro=rubro)
    prod.save()
    return render(request,r"Aplicacion1\productos.html")
