from pyexpat import model
from django.db import models
from .usuario import User
 
class Auxiliar(models.Model):
    id_auxiliar = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(User, related_name="Auxiliar", on_delete=models.CASCADE)
    