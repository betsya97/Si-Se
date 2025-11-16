from motor.motor_asyncio import AsyncIOMotorClient
from ..config import MONGO_URI, MONGO_DBNAME

client = AsyncIOMotorClient(MONGO_URI)
mongo_db = client[MONGO_DBNAME]