from rest_framework import serializers
from SHCapp.models.asignacionenfermero import asignacionenfermero
from SHCapp.serializers.userSerializer import UserSerializer
 
class AsignacionMedicoSerializer(serializers.ModelSerializer):
    id_paciente = PacienteSerializer()
    id_enfermero = EnfermeroSerializer()

    class Meta:
        model = asignacionmedico
        fields = '__all__'