from django.db import models


class Aprendiz(models.Model):
    """
    Equivalente a AprendizEntity (model/AprendizEntity.java).
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, db_column="nombre", blank=True, null=True)
    apellido = models.CharField(max_length=255, db_column="apellido", blank=True, null=True)
    cedula = models.CharField(max_length=255, db_column="cedula", blank=True, null=True)
    tipo_id = models.CharField(max_length=255, db_column="tipo_id", blank=True, null=True)
    email = models.CharField(max_length=255, db_column="email", unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=255, db_column="telefono", blank=True, null=True)
    direccion = models.CharField(max_length=255, db_column="direccion", blank=True, null=True)
    genero = models.CharField(max_length=255, db_column="genero", blank=True, null=True)
    ficha = models.CharField(max_length=255, db_column="ficha", blank=True, null=True)
    jornada = models.CharField(max_length=255, db_column="jornada", blank=True, null=True)

    class Meta:
        db_table = "aprendiz"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
