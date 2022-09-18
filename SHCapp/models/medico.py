from pyexpat import model
from django.db import models
from .usuario import User

class Medico(models.Model): 
    id_medico = models.IntegerField(primary_key=True)
    especialidad = models.CharField('especialidad', max_length=100)
    id_usuario = models.ForeignKey(User, related_name="Medico", on_delete=models.CASCADE)