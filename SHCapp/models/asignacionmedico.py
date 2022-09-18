from pyexpat import model
from django.db import models
from .usuario import User
 
class AsignacionMedico(models.Model):
    id_asignacion_medico = models.IntegerField(primary_key=True)
    id_paciente = models.ForeignKey(User, related_name="asignacionmedico", on_delete=models.CASCADE)
    id_medico = models.ForeignKey(User, related_name="asignacionmed",  on_delete=models.CASCADE)