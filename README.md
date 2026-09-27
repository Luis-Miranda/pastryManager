# 🧁 PastryManager API

API RESTful para la gestión integral de pedidos, productos, clientes e inventario de una pastelería. Construida con FastAPI y PostgreSQL, siguiendo buenas prácticas de arquitectura, autenticación y testing.

## 🚀 Stack tecnológico

- **Framework:** FastAPI
- **Base de datos:** PostgreSQL
- **ORM:** SQLAlchemy + Alembic (migraciones)
- **Autenticación:** JWT (access + refresh tokens)
- **Caché:** Redis
- **Tareas en background:** Celery / BackgroundTasks
- **Testing:** Pytest
- **Contenedores:** Docker + docker-compose

## 📦 Instalación local

\```bash
git clone https://github.com/Luis-Miranda/pastryManager.git
cd pastryManager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
\```

Documentación interactiva disponible en `http://localhost:8000/docs`.

## 🗺️ Roadmap

- [x] Configuración inicial del proyecto
- [ ] Modelos de datos (clientes, productos, pedidos)
- [ ] Conexión a PostgreSQL + migraciones con Alembic
- [ ] Autenticación JWT con roles
- [ ] Endpoints CRUD de pedidos y productos
- [ ] Webhooks salientes
- [ ] Caché con Redis
- [ ] Tareas en background
- [ ] Tests con pytest
- [ ] Dockerización y deploy

## 🏗️ Arquitectura

_(Se agregará un diagrama una vez definidos los modelos de datos)_

## 📄 Licencia

MIT