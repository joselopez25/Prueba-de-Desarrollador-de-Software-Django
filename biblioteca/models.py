from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo para representar un libro
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    año_publi = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo  # Representación en cadena del objeto

# Modelo para representar a los usuarios
class Users(AbstractUser):
    # Opciones para el campo 'rol'
    ROL_CHOICES = (
        ('usuario regular', 'Usuario Regular'),
        ('administrador', 'Administrador'),
    )
    
    # Campo para almacenar los libros prestados por el usuario
    libros_prestados = models.ManyToManyField(Libro, related_name='usuarios_prestados', null=True, blank=True)
    
    # Campo para almacenar el rol del usuario
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)