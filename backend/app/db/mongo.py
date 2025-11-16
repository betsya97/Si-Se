from motor.motor_asyncio import AsyncIOMotorClient
from ..config import MONGODB_URI, MONGO_DBNAME

client = AsyncIOMotorClient(MONGODB_URI)
mongo_db = client[MONGO_DBNAME]