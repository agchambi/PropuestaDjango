from rest_framework import serializers
from .models import Autor, Libro, Cliente, Prestamo, AutorLibro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'

class AutorLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorLibro
        fields = '__all__'
