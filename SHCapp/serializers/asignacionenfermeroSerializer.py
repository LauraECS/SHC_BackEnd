from rest_framework import serializers
from SHCapp.models.AsignacionEnfermero import AsignacionEnfermero
from SHCapp.serializers.userSerializer import UserSerializer
 
class AsignacionMedicoSerializer(serializers.ModelSerializer):
    id_paciente = PacienteSerializer()
    id_enfermero = EnfermeroSerializer()

    class Meta:
        model = AsignacionMedico
        fields = '__all__'