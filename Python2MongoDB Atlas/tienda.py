from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

cliente = MongoClient(os.getenv('MONGO_URI'))
db = cliente['tienda']

# Paso 1 — obtener el pedido
pedido = db.pedidos.find_one({"_id": 1})

# Paso 2 — usar cliente_id para buscar el cliente
cliente = db.clientes.find_one({"_id": pedido["cliente_id"]})

# Mostrar resultado combinado
print(f"Pedido : {pedido['_id']} — {pedido['estado']} — ${pedido['total']}")
print(f"Cliente: {cliente['nombre']} ({cliente['email']})")
print(f"Items : {len(pedido['items'])} producto(s)")
for item in pedido["items"]:
    print(f" · {item['nombre_producto']} x {item['cantidad']} — ${item['precio_unitario']}")