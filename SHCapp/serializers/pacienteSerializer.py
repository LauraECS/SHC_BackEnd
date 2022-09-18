from rest_framework import serializers
from SHCapp.models.Paciente import Paciente
from SHCapp.serializers.userSerializer import UserSerializer
 
class PacienteSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()
    id_cuidador = CuidadorSerializer()

    class Meta:
        model = Paciente
        fields = '__all__'