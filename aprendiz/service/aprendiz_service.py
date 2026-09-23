from ..models import Aprendiz
from ..repository import AprendizRepository


class AprendizService:
    """
    Equivalente a AprendizService (service/AprendizService.java).
    Contiene la logica de negocio del CRUD; delega la persistencia
    al repository, igual que hacia la version en Spring Boot.
    """

    def __init__(self):
        self.repository = AprendizRepository()

    def crear_aprendiz(self, aprendiz: Aprendiz) -> Aprendiz:
        return self.repository.guardar(aprendiz)

    def obtener_aprendices(self):
        return self.repository.buscar_todos()

    def buscar_aprendiz(self, id):
        return self.repository.buscar_por_id(id)

    def actualizar_aprendiz(self, id, aprendiz: Aprendiz) -> Aprendiz:
        aprendiz.id = id
        return self.repository.guardar(aprendiz)

    def eliminar_aprendiz(self, id):
        self.repository.eliminar_por_id(id)
