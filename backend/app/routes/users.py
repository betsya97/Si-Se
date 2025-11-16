from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def list_users():
    return {"message": "users endpoint works"}
