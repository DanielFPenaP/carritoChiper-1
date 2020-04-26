from django.contrib import admin

from .models import Tendero
from .models import Producto
from .models import Carrito
from .models import Pcc

admin.site.register(Tendero)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Pcc)
