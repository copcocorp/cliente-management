# clientes/models.py
from django.db import models

class Cliente(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('individual', 'Individual'),
        ('empresa', 'Empresa'),
        ('gov', 'Gubernamental'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('soltero', 'Soltero/a'),
        ('casado', 'Casado/a'),
        ('divorciado', 'Divorciado/a'),
        ('viudo', 'Viudo/a'),
    ]

    # Campos del cliente
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    tipo_cliente = models.CharField(max_length=20, choices=TIPO_CLIENTE_CHOICES, default='individual')
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    ingresos_anuales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"