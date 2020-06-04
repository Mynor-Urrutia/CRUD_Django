from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(max_length=100)
    nitCliente = models.CharField(max_length=15)
    direccionCliente = models.CharField(max_length=200)
    telefonoCliente = models.CharField(max_length=15)
    correoCliente = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombreCliente

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100)
    proveedorProducto = models.CharField(max_length=120)
    fechaProducto = models.DateField(max_length=200)
    fechaProducto = models.FloatField(max_length=10)

    def __str__(self):
        return self.nombreProducto

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombreProveedor = models.CharField(max_length=100)
    nitProveedor = models.CharField(max_length=15)
    direccionProveedor = models.CharField(max_length=200)
    telefonoProveedor = models.CharField(max_length=15)
    correoProveedor = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombreProveedor

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    nombrePersonal = models.CharField(max_length=100)
    nitPersonal = models.CharField(max_length=15)
    direccionPersonal = models.CharField(max_length=200)
    telefonoPersonal = models.CharField(max_length=15)
    correoPersonal = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombrePersonal

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    marcaVehiculo = models.CharField(max_length=100)
    modeloVehiculo = models.CharField(max_length=100)
    placaVehiculo = models.CharField(max_length=10)
    personalVehiculo = models.CharField(max_length=100)

    def __str__(self):
        return self.marcaVehiculo