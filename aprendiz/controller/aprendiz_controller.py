from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Aprendiz
from ..serializers import AprendizSerializer
from ..service import AprendizService


class AprendizListCreateView(APIView):
    """
    Equivalente a la parte del AprendizController (controller/
    AprendizController.java) que maneja:
      GET  /api/v1/aprendiz      -> lista de aprendices
      POST /api/v1/aprendiz      -> crear aprendiz
    """
    service = AprendizService()

    def get(self, request):
        aprendices = self.service.obtener_aprendices()
        serializer = AprendizSerializer(aprendices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AprendizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        nuevo_aprendiz = Aprendiz(**serializer.validated_data)
        creado = self.service.crear_aprendiz(nuevo_aprendiz)
        return Response(AprendizSerializer(creado).data, status=status.HTTP_201_CREATED)


class AprendizDetailView(APIView):
    """
    Equivalente a la parte del AprendizController que maneja:
      GET    /api/v1/aprendiz/{id}  -> buscar aprendiz por id
      PUT    /api/v1/aprendiz/{id}  -> actualizar aprendiz
      DELETE /api/v1/aprendiz/{id}  -> eliminar aprendiz
    """
    service = AprendizService()

    def get(self, request, id):
        aprendiz = self.service.buscar_aprendiz(id)
        if aprendiz is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(AprendizSerializer(aprendiz).data)

    def put(self, request, id):
        aprendiz_existente = self.service.buscar_aprendiz(id)
        if aprendiz_existente is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # Se pasa la instancia existente para que la validacion de email
        # unico no se rechace a si misma al actualizar.
        serializer = AprendizSerializer(aprendiz_existente, data=request.data)
        serializer.is_valid(raise_exception=True)
        aprendiz_actualizado = Aprendiz(**serializer.validated_data)
        actualizado = self.service.actualizar_aprendiz(id, aprendiz_actualizado)
        return Response(AprendizSerializer(actualizado).data)

    def delete(self, request, id):
        if self.service.buscar_aprendiz(id) is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        self.service.eliminar_aprendiz(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
