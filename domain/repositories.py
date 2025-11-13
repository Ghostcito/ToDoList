from abc import ABC, abstractmethod
from typing import List
from .task import Task # Importamos nuestra entidad

class TaskRepository(ABC):
    """
    Define el contrato (interfaz) para el repositorio de tareas.
    Cualquier implementación de repositorio (en memoria, SQL, NoSQL)
    debe cumplir con estos métodos.
    """

    @abstractmethod
    def add(self, task: Task) -> Task:
        """Agrega una nueva tarea."""
        pass

    @abstractmethod
    def list(self) -> List[Task]:
        """Lista todas las tareas."""
        pass