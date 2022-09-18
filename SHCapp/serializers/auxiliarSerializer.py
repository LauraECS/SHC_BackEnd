from rest_framework import serializers
from SHCapp.models.auxiliar import Auxiliar
from SHCapp.serializers.userSerializer import UserSerializer
 
class AuxiliarSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()
    
    class Meta:
        model = auxiliar
        fields = '__all__'