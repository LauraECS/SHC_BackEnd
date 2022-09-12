from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from SHCapp.models.usuario import User
from SHCapp.serializers.userSerializer import UserSerializer

class UserView(generics.RetrieveAPIView):
    queryset = User.objects.get()
    serializer_class = UserSerializer(queryset)   

    def get(self, request):   
        return Response({"status": "success", "data": self.serializer_class.data}, status=status.HTTP_200_OK)  
