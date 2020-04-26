from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto


def index(request):
    return HttpResponse("Buenaas, estas en la tienda de chiper!")

def list_productos(request):
    productos = queryset = Producto.objects.all()
    context = {
        'productos_list': productos
    }
    return render(request, 'productos.html', context)
