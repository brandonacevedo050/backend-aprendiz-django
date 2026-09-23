# Django exige que el paquete se llame "models" (en plural) para poder
# descubrir las entidades automaticamente, por eso se llama asi y no
# "model" como en el proyecto Java. Dentro, cada entidad vive en su
# propio archivo (igual que model/AprendizEntity.java).
from .aprendiz import Aprendiz

__all__ = ["Aprendiz"]
