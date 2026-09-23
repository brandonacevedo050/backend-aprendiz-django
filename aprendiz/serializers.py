from rest_framework import serializers

from .models import Aprendiz

# En el proyecto Java, Jackson serializaba/deserializaba el JSON de forma
# automatica gracias a las anotaciones de Lombok sobre AprendizEntity.
# Django REST Framework no lo hace de forma implicita, por eso necesitamos
# este serializer explicito para convertir entre JSON y el modelo Aprendiz.


class AprendizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprendiz
        fields = [
            "id",
            "nombre",
            "apellido",
            "cedula",
            "tipo_id",
            "email",
            "telefono",
            "direccion",
            "genero",
            "ficha",
            "jornada",
        ]
