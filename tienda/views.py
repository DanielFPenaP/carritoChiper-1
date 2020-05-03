from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .logic import getProductos, ProductoForm, create_producto
from django.contrib import messages
from django.urls import reverse

def index(request):
    return HttpResponse("Buenaas, estas en la tienda de chiper!")

def list_productos(request):
    if request.method == 'POST':
        dict=request.POST
        print(dict)
        messages.add_message(request, messages.SUCCESS, 'Producto -'+dict.__getitem__('id')+'- agregado')
        return HttpResponseRedirect('productos')
    else:
        productos = getProductos()
        context = {
            'productos_list': productos
        }
        return render(request, 'productos.html', context)

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            create_producto(form)
            messages.add_message(request, messages.SUCCESS, 'Producto creado')
            return HttpResponseRedirect('productos')
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form
    }

    return render(request, 'crearProducto.html', context)
