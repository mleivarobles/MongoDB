from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

cliente = MongoClient(os.getenv('MONGO_URI'))
db = cliente['persona']
coleccion = db['persona']

usuarios = coleccion.find()
print(f"Total de usuarios: {coleccion.count_documents({})}")
print("-" * 40)
for u in usuarios:
    print(f"ID: {u['_id']} | Nombre: {u.get('nombre', '-')} | Apellido: {u.get('apellido', '-')} | Edad: {u.get('edad', '-')} | Ciudad: {u.get('ciudad', '-')} | Vehiculos: {u.get('vehiculos', '-')}")
    