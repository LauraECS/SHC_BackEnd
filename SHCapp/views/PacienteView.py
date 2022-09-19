from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from SHCapp.serializers.pacienteSerializer import PacienteSerializer

class PacienteCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "nombre":request.data["nombre"],
            "apellidos":request.data["apellidos"],
            "documento":request.data["documento"],
            "direccion":request.data["direccion"],
            "telefono":request.data["telefono"],
            "genero":request.data["genero"],
            "fecha_nacimiento":request.data["fecha_nacimiento"],            
            "password":request.data["password"],
            "username":request.data["username"],
            "correo":request.data["correo"],
            "fecha_registro":request.data["fecha_registro"],
            "id_tipo_usuario":2,
            "latitud":request.data["latitud"],
            "longitud":request.data["longitud"],

            }
        
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


