from django.db import models
import uuid

class Tendero(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return "Cedula: "+str(self.cedula)+", Nombre: "+self.nombre+", Apellido: "+self.apellido


class Producto(models.Model):
    CATEGORIAS = [
        ('Frutas y verduras','Frutas y verduras'),
        ('Licores','Licores'),
        ('Cuidado personal','Cuidado personal'),
        ('Bebidas','Bebidas'),
        ('Lacteos','Lacteos'),
        ('Snacks','Snacks'),
        ('Hogar','Hogar'),
        ('Panaderia','Panaderia'),
        ('Despensa','Despensa'),
        ('Congelados','Congelados'),
        ('Pastas y granos','Pastas y granos'),
        ('Pollo, carne, pescado','Pollo, carne, pescado'),
        ('Mascotas','Mascotas'),
        ('Farmacia','Farmacia'),
        ('Otros','Otros'),
    ]

    nombre = models.CharField(max_length=100, primary_key=True)
    categoria = models.CharField(max_length=50,choices=CATEGORIAS)
    precio = models.PositiveIntegerField(default=0)
    disponibilidad = models.PositiveIntegerField(default=0)
    def __str__(self):
        return "Nombre: "+self.nombre+", Categoria: "+self.categoria+", Precio: "+str(self.precio)


class Carrito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tendero = models.ForeignKey(Tendero, on_delete=models.CASCADE)
    vendido = models.BooleanField(default=False)
    total = models.IntegerField(default=0)
    def __str__(self):
        return "id: "+str(self.id)

#Producto carro cantidad
class Pcc(models.Model):
    producto = models.ForeignKey(Producto,  on_delete=models.PROTECT)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
