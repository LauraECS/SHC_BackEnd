from rest_framework import serializers
from SHCapp.models.tipoUsuario import Tipo_Usuario

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Usuario
        fields = ['id_tipo_usuario','nombre_tipo_usuario']

