# CRUD for flashcards
from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId
from ..db.mongo import mongo_db
from ..models.mongo_models import FlashcardIn, FlashcardOut

router = APIRouter(prefix="/flashcards", tags=["flashcards"])

@router.post("/", response_model=dict)
async def create_flashcard(flashcard: FlashcardIn):
    result = await mongo_db.flashcards.insert_one(flashcard.dict())
    return {"id": str(result.inserted_id)}

@router.get("/deck/{deck}", response_model=List[dict])
async def get_by_deck(deck: str, limit: int = 100):
    cursor = mongo_db.flashcards.find({"deck": deck}).limit(limit)
    results = []
    async for document in cursor:
        document["id"] = str(document["_id"])
        document.pop("_id", None)
        results.append(document)
    return results    

@router.get("/{id}", response_model=dict)
async def get_flashcard(id: str):
    document = await mongo_db.flashcards.find_one({"_id": ObjectId(id)})
    if not document:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    document["id"] = str(document["_id"]); document.pop("_id", None)
    return document

@router.delete("/{id}",response_model=dict)
async def delete_flashcard(id: str):
    result = await mongo_db.flashcards.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return {"deleted": True}
