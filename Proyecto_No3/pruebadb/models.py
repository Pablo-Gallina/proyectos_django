from django.db import models

class Empresa(models.Model):
    # Campos
    nombre = models.CharField(max_length=20, help_text="Enter field documentation")
    fundacion = models.IntegerField()