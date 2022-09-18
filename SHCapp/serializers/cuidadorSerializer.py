from rest_framework import serializers
from SHCapp.models.Cuidador import Cuidador
from SHCapp.serializers.userSerializer import UserSerializer
 
class CuidadorSerializer(serializers.ModelSerializer):
    id_usuario = UserSerializer()
    
    class Meta:
        model = Cuidador
        fields = '__all__'