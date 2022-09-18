from rest_framework import serializers
from SHCapp.models.Enfermero import Enfermero
from SHCapp.serializers.userSerializer import UserSerializer
 
class EnfermeroSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()
    
    class Meta:
        model = Enfermero
        fields = '__all__'