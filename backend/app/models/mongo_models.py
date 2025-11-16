from pydantic import BaseModel
from typing import Optional

class FlashcardIn(BaseModel):
    question: str
    answer: str
    deck: Optional[str] = None

class FlashcardOut(FlashcardIn):
    id: str