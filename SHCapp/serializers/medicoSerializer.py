from rest_framework import serializers
from SHCapp.models.Medico import Medico
from SHCapp.serializers.userSerializer import UserSerializer

class MedicoSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()

    class Meta:
        model = Medico
        fields = '__all__'