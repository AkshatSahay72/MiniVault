from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from db import Database
from search import search_notes

app = FastAPI()
db = Database("notes.db")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    notes = db.get_all_notes()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "notes": notes}
    )

@app.post("/add")
def add_note(note: str = Form(...)):  
    db.insert_notes(note)             
    return RedirectResponse(url="/", status_code=303)

@app.get("/search")
def search(query: str):
    notes = db.get_all_notes()

    if not notes:
        return {"results": []}

    note_texts = [n[1] for n in notes]

    results = search_notes(query, note_texts)

    response = []
    for idx, score in results:
        response.append({
            "note": note_texts[idx],
            "score": float(score)
        })

    return {"results": response}