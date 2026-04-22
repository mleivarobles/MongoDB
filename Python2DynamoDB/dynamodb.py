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

tabla = dynamodb.Table('personas')
print(tabla.table_status)

# Leer todos los usuarios
def listar_usuarios():
    respuesta = tabla.scan()
    personas = respuesta['Items']
    print(f"Total de personas: {len(personas)}")
    print("-" * 40)
    for u in personas:
        print(f"ID: {u['rut']} | nombre: {u.get('nombre')} | edad: {u.get('edad')} | ciudad: {u.get('ciudad')}")

        vehiculos = u.get('vehiculos')
        if vehiculos is not None: #objeto nul
            for v in vehiculos:
                print(f"vehiculos: {v}")
        print()

listar_usuarios()
print()