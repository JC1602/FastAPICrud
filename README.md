<# 🛠️ FastAPI CRUD + Firestore

Este es un proyecto backend desarrollado con [FastAPI](https://fastapi.tiangolo.com/) que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) sobre un recurso llamado `items`. Usa un diccionario como base de datos inicial y se conecta con **Firestore** para persistencia en la nube.

---

## 🚀 Endpoints

| Método | Ruta                | Descripción                 |
|--------|---------------------|-----------------------------|
| POST   | `/items/`           | Crear un nuevo item         |
| GET    | `/items/`           | Obtener todos los items     |
| GET    | `/items/{item_id}`  | Obtener un item por ID      |
| PUT    | `/items/{item_id}`  | Actualizar un item completo |
| PATCH  | `/items/{item_id}`  | Actualizar parcialmente     |
| DELETE | `/items/{item_id}`  | Eliminar un item            |

---

## 🔧 Tecnologías usadas

- Python 3.12
- FastAPI
- Uvicorn
- Firestore (Firebase)
- Pydantic


---

## ⚙️ Instalación y uso

1. Clona el repositorio

2. Crea un entorno virtual

python -m venv .venv

3. Activa el entorno virtual

.venv\Scripts\Activate.ps1

4. instala dependencias

pip install -r requirements.txt


