# Sí Se
# 🧠 Flashcard App

A full-stack flashcard learning application built with **FastAPI**, **MongoDB**, **SQLAlchemy**, and **React**.  
Users can create, view, and study flashcards stored in MongoDB, while user stats and progress are tracked in an SQL database.

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React + TypeScript + Material UI |
| **Backend** | FastAPI (Python) |
| **Databases** | MongoDB (Flashcards) + PostgreSQL/SQLite (User stats) |
| **ORM / ODM** | SQLAlchemy


---

## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create Virtual Environment & Install Dependencies

```bash
#Python env variables and dependencies
cd backend
python3 -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install fastapi uvicorn motor sqlalchemy psycopg2-binary pydantic[dotenv]
```
---

### 2️⃣ Run MongoDB & SQL (SQLite or PostgreSQL)
```bash
# MongoDB: Start your local or Docker MongoDB instance.
# for Mac silicon, on a separate terminal window run:
sudo mongod --dbpath=/Users/username/data/db
```
SQL: SQLite runs automatically, or update the DB URL in sql.py for PostgreSQL/MySQL.

### 3️⃣ Run the API Server
```bash
uvicorn app.main:app --reload

#macos, run:
python3 -m uvicorn app.main:app --reload
```
API will be live at:
➡️ http://localhost:8000

Interactive API docs:
➡️ http://localhost:8000/docs
