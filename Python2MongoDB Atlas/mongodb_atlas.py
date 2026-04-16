from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

cliente = MongoClient(os.getenv('MONGO_URI'))
db = cliente['venta']
coleccion = db['usuarios']
#print(db.list_collection_names())

# Insertar un usuario
def agregar_usuario(usuario_id, nombre, apellido, edad):
    coleccion.insert_one({
        'usuario_id': usuario_id,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
    })
    print(f"Usuario {nombre} insertado")

# Insertar varios de una vez
def agregar_varios():
    coleccion.insert_many([
        {'usuario_id': 1, 'nombre': 'Juan',  'apellido': 'Soto', 'edad': None},
        {'usuario_id': 3, 'nombre': 'Sofia', 'apellido': None,   'edad': 66}
    ])
    print("Usuarios insertados")

def listar_usuarios():
    usuarios = coleccion.find()
    print(f"Total de usuarios: {coleccion.count_documents({})}")
    print("-" * 40)
    for u in usuarios:
        print(f"ID: {u['usuario_id']} | Nombre: {u.get('nombre', '-')} | Apellido: {u.get('apellido', '-')} | Edad: {u.get('edad', '-')}")

def obtener_usuario(usuario_id):
    usuario = coleccion.find_one({'usuario_id': usuario_id})
    if usuario:
        print(f"Usuario encontrado: {usuario}")
    else:
        print(f"No existe usuario con ID {usuario_id}")

#agregar_varios()
#agregar_usuario(5, 'Diego',None, None)
listar_usuarios()
obtener_usuario(5)
