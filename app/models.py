from django.db import models

# Create your models here.


class Arriendo(models.Model):
    id_arriendo = models.CharField(primary_key=True, max_length=30)  # This field type is a guess.
    fecha_inicio = models.DateField()  # This field type is a guess.
    fecha_termino = models.DateField()  # This field type is a guess.
    descripcion_arriendo = models.TextField()
    descripcion_tipo_pago = models.CharField(max_length=50)  # This field type is a guess.
    imagen = models.ImageField(upload_to="arriendo", null=True)

    def __str__(self):
        return self.id_arriendo

    


class Cliente(models.Model):
    id_rut = models.CharField(primary_key=True, max_length=11, unique=True)  # This field type is a guess.
    nombre = models.CharField(max_length=50)  # This field type is a guess.
    apellido = models.CharField(max_length=50)  # This field type is a guess.
    edad = models.IntegerField()
    sexo = models.CharField(max_length=9)  # This field type is a guess.
    correo = models.EmailField()  # This field type is a guess.
    telefono = models.IntegerField()
    arriendo = models.ForeignKey(Arriendo, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


opciones_consultas = [
    [0, "CONSULTAS"],
    [1, "RECLAMOS"],
    [2, "SUGERENCIAS"],
    [3, "FELICITACIONES"]
    
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_registro = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre