from .models import Producto
from django import forms


def getProductos():
    return Producto.objects.all()


def create_producto(form):
    producto = form.save()
    producto.save()
    return ()



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'categoria',
            'precio',
            'disponibilidad',
        ]

        labels = {
              'nombre' : 'Nombre del producto',
             'categoria' : 'Categoria',
             'precio' : 'Precio de venta',
             'disponibilidad' : 'Unidades disponibles',
        }
