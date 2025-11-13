## **1. Responsabilidades de las Capas**
En esta arquitectura, cada capa tiene un rol específico para mantener el código ordenado:

**Capa de Dominio** (domain): Es el núcleo del sistema. Aquí definimos qué es una tarea (Entidad Task) y las reglas de cómo debe guardarse (la interfaz TaskRepository), sin importar la tecnología. Es la capa más pura y no depende de librerías externas.

**Capa de Aplicación** (application): Contiene la lógica de negocio o "Casos de Uso" (CreateTaskUseCase, ListTasksUseCase). Su responsabilidad es coordinar: recibe una petición, llama al repositorio y devuelve el resultado. Es el puente entre el usuario y el dominio.

**Capa de Infraestructura** (infrastructure): Se encarga de los detalles técnicos. Aquí implementamos el repositorio real (InMemoryTaskRepository) que define cómo se guardan los datos (en este caso, en una lista en memoria).

**Capa de Presentación** (presentation): Es la cara visible al exterior. Usamos FastAPI para recibir las peticiones HTTP (POST/GET), convertir los datos y entregarlos al usuario.

## **2. Ventajas de esta Arquitectura**
Aplicar Clean Architecture en este ejercicio ofrece beneficios claros frente a poner todo en un solo archivo:

**Independencia de Frameworks y Bases de Datos:** Si mañana queremos cambiar la base de datos (de memoria a PostgreSQL) o el framework web (de FastAPI a Flask), no necesitamos tocar la lógica de negocio (Dominio). Solo cambiamos la capa de Infraestructura o Presentación.

**Facilidad de Pruebas (Testing):** Al tener los casos de uso desacoplados, podemos probar la lógica de "crear tarea" sin necesidad de levantar un servidor web ni una base de datos real.

**Mantenibilidad:** El código está organizado. Si hay un error en cómo se guardan los datos, sabemos que debemos buscar en infrastructure; si hay un error en la validación del JSON, buscamos en presentation.

## **3. Posibles Mejoras**
Aunque el sistema funciona, para llevarlo a producción se podrían implementar estas mejoras:

**Persistencia Real:** Reemplazar el InMemoryTaskRepository por una implementación que use una base de datos real (como PostgreSQL o SQLite) para que la información no se pierda al reiniciar el servidor.

**Inyección de Dependencias Automática:** Utilizar el sistema de inyección de dependencias de FastAPI (Depends) para gestionar la instancia del repositorio de manera más eficiente, en lugar de instanciarlo manualmente en api.py.

**Manejo de Excepciones:** Agregar validaciones en los casos de uso (por ejemplo, impedir tareas vacías) y capturar esos errores en la capa de presentación para devolver códigos HTTP adecuados (como 400 Bad Request).