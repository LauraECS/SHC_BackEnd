from pyexpat import model
from django.db import models
from .usuario import User
 
class Cuidador(models.Model):
    id_cuidador = models.IntegerField(primary_key=True)
    parentesco = models.CharField('parentesco',max_length=100)
    id_usuario = models.ForeignKey(User, related_name="Cuidador", on_delete=models.CASCADE)
    