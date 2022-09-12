from django.db import models

class Tipo_Usuario(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True)
    nombre_tipo_usuario = models.CharField('nombre_tipo_usuario', max_length=100)