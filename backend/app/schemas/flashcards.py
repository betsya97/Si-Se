from pydantic import BaseModel

class FlashcardBase(BaseModel):
    question: str
    answer: str

class FlashcardCreate(FlashcardBase):
    pass

class FlashcardOut(FlashcardBase):
    id: int | None = None

    class Config:
        from_attributes = True
