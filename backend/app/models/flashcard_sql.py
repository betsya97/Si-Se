from sqlalchemy import Column, Integer, String
from app.db.sql import Base

class FlashcardSQL(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
