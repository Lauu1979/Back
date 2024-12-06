from motor.motor_asyncio import AsyncIOMotorClient  # Para conexión asíncrona con MongoDB
from fastapi import Depends

# URI de conexión a MongoDB Atlas (reemplaza las credenciales si es necesario)
MONGODB_URL = "mongodb+srv://laurabohorquezpabon123:pBW3LjPURK95f3um@cluster0.4gmxd.mongodb.net/Entry-Solution?retryWrites=true&w=majority&appName=Cluster0"

# Crear cliente asíncrono de MongoDB
client = AsyncIOMotorClient(MONGODB_URL)

# Seleccionar la base de datos
db = client["Entry-Solution"]

# Función para obtener la base de datos
async def get_db():
    try:
        yield db
    finally:
        # Aquí puedes manejar cierre de conexiones si es necesario
        pass