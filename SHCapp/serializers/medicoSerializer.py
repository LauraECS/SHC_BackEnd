from rest_framework import serializers
from SHCapp.models.medico import Medico
from SHCapp.serializers.userSerializer import UserSerializer

class MedicoSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()
    class Meta:
        model = Medico
        fields = ['id_medico', 'especialidad', 'id_usuario']