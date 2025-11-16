from pathlib import Path
from dotenv import load_dotenv
import os 

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
MONGO_DBNAME = os.getenv('DATABASE_NAME', 'flashcards_db')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///flashcards.db')