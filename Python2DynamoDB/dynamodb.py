from dotenv import load_dotenv
import boto3, os

load_dotenv()

dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv('AWS_DEFAULT_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN')
)

tabla = dynamodb.Table('usuarios')
print(tabla.table_status)

# Leer todos los usuarios
def listar_usuarios():
    respuesta = tabla.scan()
    usuarios = respuesta['Items']
    print(f"Total de usuarios: {len(usuarios)}")
    print("-" * 40)
    for u in usuarios:
        print(f"ID: {u['usuario_id']} | Nombre: {u.get('nombre', '-')} | Apellido: {u.get('apellido', '-')} | Edad: {u.get('edad', '-')}")

# Leer un usuario por ID
def obtener_usuario(usuario_id):
    respuesta = tabla.get_item(Key={'usuario_id': usuario_id})
    usuario = respuesta.get('Item')
    if usuario:
        print(f"Usuario encontrado: {usuario}")
    else:
        print(f"No existe usuario con ID {usuario_id}")

listar_usuarios()
print()
#obtener_usuario(1)   # Juan Soto
#obtener_usuario(3)   # Sofia