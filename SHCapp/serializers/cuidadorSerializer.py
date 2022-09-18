from rest_framework import serializers
from SHCapp.models.cuidador import Cuidador
from SHCapp.serializers.userSerializer import UserSerializer
 
class CuidadorSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()
    
    class Meta:
        model = cuidador
        fields = '__all__'