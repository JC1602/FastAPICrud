## 🧑‍💻 Creadores

- Juan Pablo Idarraga Pabon  
- Jean Carlo Londoño Neira

<# 🛠️ FastAPI CRUD + Firestore

Este es un proyecto backend desarrollado con [FastAPI](https://fastapi.tiangolo.com/) que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) sobre un recurso llamado `items`. Los datos se almacenan de forma persistente en la nube utilizando **Firestore** como base de datos NoSQL de Google Cloud.

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

# En Windows PowerShell
.venv\Scripts\Activate.ps1

# En macOS/Linux
source .venv/bin/activate

3. Activa el entorno virtual

.venv\Scripts\Activate.ps1

4. instala dependencias

pip install -r requirements.txt

5. Configura tu archivo .env con la ruta a tu clave de servicio de Firebase:

FIREBASE_KEY_PATH= tu/ruta/firebase-key.json


---

## ☁️ Despliegue
Puedes acceder a la documentación de la API desplegada en la nube desde:

🔗 https://fastapi-3wlsx5wld-juan-idarragas-projects.vercel.app/docs


