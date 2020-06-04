from django.contrib import admin
from .models import Cliente
from .models import Personal
from .models import Productos
from .models import Proveedor
from .models import Vehiculo

admin.site.register(Cliente)
admin.site.register(Personal)
admin.site.register(Productos)
admin.site.register(Proveedor)
admin.site.register(Vehiculo)
