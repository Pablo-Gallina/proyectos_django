from django.db import models

class Empresa(models.Model):
    # Campos
    nombre = models.CharField(max_length=20, help_text="Enter field documentation")
    fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=40)
    creador = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.nombre
    
class Programador(models.Model):
    nombre = models.CharField(max_length=20, help_text="Enter field documentation")
    edad = models.IntegerField(null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,  related_name="empleados") #SET_NULL para que cuando se borre la fk, el registro siga existiendo
    lenguaje = models.ManyToManyField(Lenguaje)
    
    def __str__(self):
        return self.nombre
    
        