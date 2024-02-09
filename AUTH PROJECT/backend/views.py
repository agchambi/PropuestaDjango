from rest_framework import generics
from .models import Autor, Libro, Cliente, Prestamo, AutorLibro
from .serializers import AutorSerializer, LibroSerializer, ClienteSerializer, PrestamoSerializer, AutorLibroSerializer

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PrestamoList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class PrestamoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class AutorLibroList(generics.ListCreateAPIView):
    queryset = AutorLibro.objects.all()
    serializer_class = AutorLibroSerializer

class AutorLibroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AutorLibro.objects.all()
    serializer_class = AutorLibroSerializer
