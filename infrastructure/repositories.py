from typing import List
from domain.task import Task
from domain.repositories import TaskRepository

class InMemoryTaskRepository(TaskRepository):
    """
    Implementación concreta del repositorio que guarda las tareas
    en una lista en la memoria RAM (se borran al reiniciar).
    """
    def __init__(self):
        self.tasks = [] # Aquí se guardarán las tareas

    def add(self, task: Task) -> Task:
        self.tasks.append(task)
        return task

    def list(self) -> List[Task]:
        return self.tasks