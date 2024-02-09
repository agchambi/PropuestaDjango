from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    lote = models.CharField(max_length=255)
    descripcion = models.TextField()
    isActive = models.BooleanField(default=True)
    autores = models.ManyToManyField(Autor, through='AutorLibro')

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    dias_prestamo = models.PositiveIntegerField()
    estado = models.SmallIntegerField(default=0)
    isActive = models.BooleanField(default=True)

class AutorLibro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

