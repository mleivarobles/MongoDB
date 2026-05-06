from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

cliente = MongoClient(os.getenv('MONGO_URI'))
db = cliente['biblioteca']

#todos los socios
print()
for s in db.socios.find():
    #print (s)
    print(f"[{s['_id']}] {s['nombre']} — {s['email']} - {s['telefono']} - {s['fecha_inscripcion']}")

#todos los libros y autores
print()
for l in db.libros.find():
    #print(l)
    print(f"libro: {l['titulo']} - {l['genero']} - {l['anio_publicacion']} y stock= {l['stock']}")
    for a in l.get("autores"):
        print(f"  autores: {a['nombre']}")

#todos los prestamos
print()
for p in db.prestamos.find().sort("_id",1):
    #print(p)
    titulo  = p.get("libro").get("titulo") 
    nro_socio = int(p.get("socio_id"))
    socio = db.socios.find_one({"_id": nro_socio})
    
    n_multas = len(p.get("multas"))
    s_prestamo = f"El libro '{titulo}' fue prestado a {socio['nombre']}"

    if n_multas == 0:
        print(f"{s_prestamo} y no tiene multas")
    else:
        lst_multa = p.get("multas")[0] #imprime el primer elemento
        monto = lst_multa.get("monto")
        motivo = lst_multa.get("motivo")
        print(f"{s_prestamo} y tiene un multa de {monto} y por {motivo}")
        