from pyexpat import model
from django.db import models
from .usuario import User
 
class AsignacionEnfermero(models.Model):
    id_asignacion_enfermero = models.IntegerField(primary_key=True)
    id_paciente = models.ForeignKey(User, related_name="asignacionenfermero", on_delete=models.CASCADE)
    id_enfermero = models.ForeignKey(User, related_name="asignacionenf",  on_delete=models.CASCADE)