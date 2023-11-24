from django.shortcuts import render
from rest_framework import generics 
from .models import Producto
from .serializers import ProductoSerializer


# Create your views here.

# Listar y crear productos
class ProductoLista(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# Puedo actualizar y eliminar productos especificos
class ProductoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer