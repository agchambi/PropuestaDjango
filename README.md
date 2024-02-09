# Reflexiones sobre el Rediseño de la Base de Datos y el Desarrollo Backend

## Rediseño de la Base de Datos

El proceso de rediseño de la base de datos fue un paso inicial crucial en nuestro proyecto. La necesidad de este rediseño nació de la visión de futuro para el almacenamiento de datos, especialmente en lo que respecta a la inclusión de nuevos valores y resultados. Este enfoque proactivo no solo mejora la integridad y la accesibilidad de los datos en el presente sino que también sienta las bases para una gestión de datos más sofisticada en el futuro.

## Elección de Tecnología para el Backend

Para el desarrollo del backend, he optado por utilizar **Django**, un framework de Python reconocido por su popularidad y eficiencia. La elección de Python como lenguaje de programación subyace en su vasto potencial para el desarrollo backend, característica que considero fundamental para la escalabilidad y adaptabilidad del proyecto a largo plazo.

Mirando hacia el futuro, estoy consciente de que el proyecto tiene el potencial de expandirse significativamente. Por lo tanto, la flexibilidad y robustez de Django ofrecen una base sólida sobre la cual podemos construir y evolucionar, añadiendo nuevas funcionalidades según sea necesario.

## Diseño y Desarrollo de Microservicios

En lo que respecta al diseño y desarrollo de microservicios, mi enfoque se centra en los principios de **Alta Cohesión (High Cohesion)** y **Bajo Acoplamiento (Low Coupling)**. Esta metodología no solo es práctica sino también esencial para mantener una arquitectura de software manejable y escalable. Sin embargo, soy consciente de que el desarrollo de microservicios requiere tiempo y dedicación, y valoraría la oportunidad de invertir más en esta área.

La implementación de microservicios, en mi experiencia, facilita significativamente el mantenimiento de aplicaciones, especialmente aquellas que están en uso constante. Este enfoque modular permite actualizaciones y mejoras continuas sin interrumpir el funcionamiento global del sistema.

## Influencias y Mentores

Por último, mi enfoque y comprensión del desarrollo de software han sido enriquecidos significativamente por mi mentor, **Phil Sturgeon**, y su obra *"APIs You Won't Hate"*. Este libro se ha convertido en una herramienta invaluable para mí y, creo, para cualquier desarrollador que se adentra en el complejo mundo de la ingeniería del software. Su perspectiva y consejos han sido fundamentales en mi desarrollo profesional y en la manera en que abordo los desafíos del desarrollo de backend.

## URLs y Endpoints de la API

A continuación se detallan las rutas disponibles en la aplicación, que corresponden a las funcionalidades para `Autores`, `Libros`, `Clientes`, `Prestamos` y `AutorLibro`:

### URLs para Autor
- `GET /autores/`: Listar todos los autores.
- `POST /autores/`: Crear un nuevo autor.
- `GET /autores/<int:pk>/`: Obtener detalles de un autor específico.
- `PUT /autores/<int:pk>/`: Actualizar un autor existente.
- `DELETE /autores/<int:pk>/`: Eliminar un autor.

### URLs para Libro
- `GET /libros/`: Listar todos los libros.
- `POST /libros/`: Crear un nuevo libro.
- `GET /libros/<int:pk>/`: Obtener detalles de un libro específico.
- `PUT /libros/<int:pk>/`: Actualizar un libro existente.
- `DELETE /libros/<int:pk>/`: Eliminar un libro.

### URLs para Cliente
- `GET /clientes/`: Listar todos los clientes.
- `POST /clientes/`: Crear un nuevo cliente.
- `GET /clientes/<int:pk>/`: Obtener detalles de un cliente específico.
- `PUT /clientes/<int:pk>/`: Actualizar un cliente existente.
- `DELETE /clientes/<int:pk>/`: Eliminar un cliente.

### URLs para Prestamo
- `GET /prestamos/`: Listar todos los préstamos.
- `POST /prestamos/`: Crear un nuevo préstamo.
- `GET /prestamos/<int:pk>/`: Obtener detalles de un préstamo específico.
- `PUT /prestamos/<int:pk>/`: Actualizar un préstamo existente.
- `DELETE /prestamos/<int:pk>/`: Eliminar un préstamo.

### URLs para AutorLibro
- `GET /autorlibro/`: Listar todas las relaciones Autor-Libro.
- `POST /autorlibro/`: Crear una nueva relación Autor-Libro.
- `GET /autorlibro/<int:pk>/`: Obtener detalles de una relación Autor-Libro específica.
- `PUT /autorlibro/<int:pk>/`: Actualizar una relación Autor-Libro existente.
- `DELETE /autorlibro/<int:pk>/`: Eliminar una relación Autor-Libro.
