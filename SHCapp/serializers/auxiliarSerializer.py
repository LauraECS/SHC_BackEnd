from rest_framework import serializers
from SHCapp.models.Auxiliar import Auxiliar
from SHCapp.serializers.userSerializer import UserSerializer
 
class AuxiliarSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()
    
    class Meta:
        model = Auxiliar
        fields = '__all__'