from domain.task import Task
from domain.repositories import TaskRepository
from typing import List

class CreateTaskUseCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(self, title: str) -> Task:
        # Creamos la entidad Task aquí (el ID se genera solo)
        task = Task(title=title)
        # Usamos el repositorio para guardarla
        return self.repository.add(task)

class ListTasksUseCase:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def execute(self) -> List[Task]:
        # Simplemente pedimos al repositorio que nos dé la lista
        return self.repository.list()