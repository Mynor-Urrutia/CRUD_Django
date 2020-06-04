from django.shortcuts import render
from .models import Cliente
from .models import Proveedor
from .models import Personal
from .models import Productos
from .models import Vehiculo


def inicio(request):
    return render(request, 'index.html')


def pclientes(request):
    clientes = Cliente.objects.all()
    contexto = {
        'clientes': clientes
    }
    return render(request, 'clientes.html', contexto)


def ppersonal(request):
    personals = Personal.objects.all()
    contexto = {
        'personals': personals
    }
    return render(request, 'personal.html', contexto)


def pproductos(request):
    producto = Productos.objects.all()
    context = {
        'producto': producto
    }
    return render(request, 'productos.html', context)


def pproveedor(request):
    proveedor = Proveedor.objects.all()
    context = {
        'proveedor': proveedor
    }
    return render(request, 'proveedor.html', context)


def pvehiculos(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculo': vehiculos
    }
    return render(request, 'vehiculos.html', context)
