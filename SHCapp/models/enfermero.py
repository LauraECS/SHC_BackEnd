from pyexpat import model
from django.db import models
from .usuario import User
 
class Enfermero(models.Model):
    id_enfermero = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(User, related_name="Enfermero", on_delete=models.CASCADE)