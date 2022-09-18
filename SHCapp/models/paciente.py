from pyexpat import model
from django.db import models
from .usuario import User
 
class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    latitud = models.CharField('latitud', max_length=100, null=True)
    longitud = models.CharField('longitud', max_length=100, null=True)
    id_usuario = models.ForeignKey(User, related_name="UsarioPaciente", on_delete=models.CASCADE)
    id_cuidador = models.ForeignKey(User, related_name="CuidadorPaciente", on_delete=models.CASCADE)