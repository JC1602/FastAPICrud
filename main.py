from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import Optional
from google.cloud import firestore
from google.oauth2 import service_account
from dotenv import load_dotenv

import os

load_dotenv()

# Leer la ruta del archivo JSON desde el entorno
firebase_key_path = os.getenv("FIREBASE_KEY_PATH")
# Crear credenciales
credentials = service_account.Credentials.from_service_account_file(firebase_key_path)
app = FastAPI()
db = firestore.Client(credentials=credentials)


# Modelo de datos
class Item(BaseModel):
    nombre: str
    precio: float
    stock: int

class ItemUpdate(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None

# Crear un nuevo item
@app.post("/items/")
def create_item(item: Item):
    doc_ref = db.collection("items").document()
    doc_ref.set(item.model_dump())
    return {"id": doc_ref.id, "item": item}

# Obtener todos los items
@app.get("/items/")
def get_all_items():
    docs = db.collection("items").stream()
    items = {doc.id: doc.to_dict() for doc in docs}
    return items

# Obtener un item por ID
@app.get("/items/{item_id}")
def get_item(item_id: str):
    doc = db.collection("items").document(item_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return doc.to_dict()

# Actualizar un item completamente
@app.put("/items/{item_id}")
def update_item(item_id: str, updated_item: Item):
    doc_ref = db.collection("items").document(item_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    doc_ref.set(updated_item.model_dump())
    return {"id": item_id, "item": updated_item}

# Eliminar un item
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    doc_ref = db.collection("items").document(item_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    deleted_data = doc.to_dict()
    doc_ref.delete()
    return {
        "message": "Item eliminado",
        "id": item_id,
        "nombre": deleted_data["nombre"]
    }

# Actualizar parcialmente un item
@app.patch("/items/{item_id}")
def patch_item(item_id: str, item_update: ItemUpdate):
    doc_ref = db.collection("items").document(item_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    updated_data = item_update.model_dump(exclude_unset=True)
    doc_ref.update(updated_data)
    return {"id": item_id, "actualizado": updated_data}