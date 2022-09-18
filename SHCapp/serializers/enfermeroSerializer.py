from rest_framework import serializers
from SHCapp.models.enfermero import Enfermero
from SHCapp.serializers.userSerializer import UserSerializer
 
class EnfermeroSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()
    
    class Meta:
        model = enfermero
        fields = '__all__'