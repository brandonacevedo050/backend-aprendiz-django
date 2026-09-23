from ..models import Aprendiz


class AprendizRepository:
    """
    Equivalente a AprendizRepository (repository/AprendizRepository.java,
    que extendia JpaRepository). Aqui se concentra todo el acceso directo
    al ORM/base de datos para la entidad Aprendiz.
    """

    def guardar(self, aprendiz: Aprendiz) -> Aprendiz:
        aprendiz.save()
        return aprendiz

    def buscar_todos(self):
        return Aprendiz.objects.all()

    def buscar_por_id(self, id):
        return Aprendiz.objects.filter(id=id).first()

    def eliminar_por_id(self, id):
        Aprendiz.objects.filter(id=id).delete()
