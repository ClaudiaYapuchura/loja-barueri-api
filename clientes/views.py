from django.shortcuts import render
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from rest_framework import viewsets

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer