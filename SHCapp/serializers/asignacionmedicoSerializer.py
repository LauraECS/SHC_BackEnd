from rest_framework import serializers
from SHCapp.models.AsignacionMedico import AsignacionMedico
from SHCapp.serializers.userSerializer import UserSerializer
 
class AsignacionMedicoSerializer(serializers.ModelSerializer):
    id_paciente = PacienteSerializer()
    id_medico = MedicoSerializer()

    class Meta:
        model = AsignacionMedico
        fields = '__all__'