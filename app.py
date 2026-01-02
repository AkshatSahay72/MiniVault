from fastapi import FastAPI
from db import Database

app = FastAPI()

# initialize database
db = Database("notes.db")


@app.post("/notes")
def add_note(note: dict):
    # expects: { "content": "some text" }
    text = note.get("content")
    db.insert_notes(text)
    return {"status": "note added"}


@app.get("/notes")
def get_notes():
    notes = db.get_all_notes()
    return {"notes": notes}
