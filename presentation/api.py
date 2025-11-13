from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Importamos las capas anteriores
from domain.task import Task
from infrastructure.repositories import InMemoryTaskRepository
from application.use_cases import CreateTaskUseCase, ListTasksUseCase

# Inicializamos la aplicación FastAPI
app = FastAPI()

# INSTANCIACIÓN DE DEPENDENCIAS (El "Wiring" o cableado)
# Creamos una única instancia del repositorio para mantener los datos en memoria
# mientras la app esté corriendo.
repository = InMemoryTaskRepository()

# Inicializamos los casos de uso con el repositorio
create_task_use_case = CreateTaskUseCase(repository)
list_tasks_use_case = ListTasksUseCase(repository)

# --- Modelos de Entrada (DTOs) ---
# Creamos un modelo solo para recibir el título, así el usuario no envía ID ni status.
class TaskCreateRequest(BaseModel):
    title: str

# --- ENDPOINTS ---

@app.post("/tasks", response_model=Task)
def create_task(request: TaskCreateRequest):
    """
    Endpoint para crear una nueva tarea.
    Recibe un JSON con 'title' y devuelve la tarea creada.
    """
    # Llamamos al caso de uso
    return create_task_use_case.execute(request.title)

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    """
    Endpoint para listar todas las tareas.
    """
    # Llamamos al caso de uso
    return list_tasks_use_case.execute()