# Gestión de Clientes y Reservas con FastAPI y MySQL

## Descripción del Proyecto

Este proyecto desarrolla una API RESTful utilizando FastAPI para gestionar una relación entre clientes y reservas. La API implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) utilizando una arquitectura basada en capas. La base de datos MySQL se gestiona con Docker Desktop, y SQLAlchemy se usa para definir los modelos de datos y manejar las migraciones con Alembic.

## Estructura del Proyecto

El proyecto está organizado en las siguientes capas:

- **Capa de Presentación (Routes/Controllers)**: Manejo de las rutas HTTP.
- **Capa de Servicio (Services)**: Contiene la lógica de negocio.
- **Capa de Persistencia (Repositories/ORM Models)**: Maneja la comunicación con la base de datos.
- **Capa de Esquemas (Schemas)**: Define los modelos de Pydantic para validación de datos.

## Modelos de Datos

**Tabla `clients` (Clientes):**
- `id`: Identificador único del cliente (entero, clave primaria).
- `full_name`: Nombre completo del cliente (cadena de caracteres).
- `phone_number`: Número de teléfono del cliente (cadena de caracteres, único).
- `email`: Correo electrónico del cliente (cadena de caracteres, único).

**Tabla `reservations` (Reservas):**
- `id`: Identificador único de la reserva (entero, clave primaria).
- `reservation_code`: Código único de la reserva (cadena de caracteres, único).
- `date`: Fecha de la reserva (fecha).
- `client_id`: Identificador del cliente que hizo la reserva (entero, clave foránea relacionada con `clients.id`).

Las tablas `clients` y `reservations` están relacionadas mediante una relación uno-a-muchos.

## Requerimientos de la API

**Rutas para `clients`:**
- `GET /clients/`: Obtener una lista de todos los clientes.
- `POST /clients/`: Crear un nuevo cliente.
- `DELETE /clients/{client_id}`: Eliminar un cliente por su ID (si un cliente tiene reservas, no debe poder ser eliminado).

**Rutas para `reservations`:**
- `GET /reservations/`: Obtener una lista de todas las reservas.
- `POST /reservations/`: Crear una nueva reserva.
- `DELETE /reservations/{reservation_id}`: Eliminar una reserva por su ID.

## Reglas de Negocio

- **Eliminación de Clientes**: Un cliente no puede ser eliminado si tiene reservas asociadas. Se devuelve un mensaje de error indicando que el cliente tiene reservas activas.
- **Unicidad de Teléfono y Correo Electrónico**: Los campos `phone_number` y `email` en la tabla `clients` deben ser únicos.
- **Unicidad del Código de Reserva**: El campo `reservation_code` en la tabla `reservations` debe ser único.
- **Validación de Fecha de Reserva**: La fecha de la reserva debe ser futura.
- **Relación Cliente-Reserva**: Al crear una reserva, se verifica que el `client_id` corresponda a un cliente existente.
- **Máximo de Reservas por Cliente**: Un cliente no puede tener más de 5 reservas activas.

## Configuración del Entorno

### Docker

1. **Construir la Imagen Docker:**
   ```bash
   docker build -t fastapi-project .
Base de Datos MySQL
Configurar MySQL con Docker: En tu docker-compose.yml, puedes definir el servicio para MySQL:

yaml
Copiar código
version: '3.1'

services:
  db:
    image: mysql:5.7
    container_name: prueba
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: parcialDedinitivo2
      MYSQL_USER: root
      MYSQL_PASSWORD: 12345
    ports:
      - "3306:3306"
Iniciar MySQL:

bash
Copiar código
docker-compose up -d
Migraciones con Alembic
Inicializar Alembic:

bash
Copiar código
alembic init alembic
Generar una Nueva Migración:

bash
Copiar código
alembic revision --autogenerate -m "Create clients and reservations tables"
Aplicar la Migración:

bash
Copiar código
alembic upgrade head
Ejecución de la API
Iniciar el Servidor de FastAPI: Asegúrate de que el contenedor de Docker esté en ejecución y que la base de datos MySQL esté operativa.

Acceder a la API: Abre tu navegador y ve a 127.0.0.1:8000/docs para interactuar con la API.
