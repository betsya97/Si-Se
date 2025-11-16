from fastapi import FastAPI
from app.routes import flashcards, users
from app.config import MONGODB_URI

# Initialize FastAPI app
app = FastAPI(title="Sí Se Flashcard App", description="A flashcard learning app with MongoDB and PostgreSQL integration.")

# Include routes
app.include_router(flashcards.router)
app.include_router(users.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Sí Se Flashcard App!"}