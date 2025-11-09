# clientes/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Cliente eliminado correctamente'}, status=status.HTTP_200_OK)