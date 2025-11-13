from pydantic import BaseModel, Field
import uuid # Usaremos UUID para los IDs

class Task(BaseModel):
    """
    Esta es la entidad principal 'Task' de nuestro dominio.
    """
    # Usamos Field para configurar el valor por defecto
    # y default_factory para generar un nuevo UUID cada vez
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str
    done: bool = False # Por defecto, una tarea nueva no está completada