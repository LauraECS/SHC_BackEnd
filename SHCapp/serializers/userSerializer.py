from rest_framework import serializers
from SHCapp.models.usuario import User
from SHCapp.serializers.tipoUsuarioSerializer import TipoUsuarioSerializer

class UserSerializer(serializers.ModelSerializer):
    id_tipo_usuario = TipoUsuarioSerializer()
    class Meta:
        model = User
        fields = ['id','nombre', 'apellidos', 'documento', 'direccion', 'telefono', 'genero', 'fecha_nacimiento', 'contrasena', 'correo', 'fecha_registro', 'id_tipo_usuario']
