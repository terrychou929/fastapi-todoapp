from fastapi import FastAPI, Request, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple TODO App")

templates = Jinja2Templates(directory="app/templates")

# 跨域（選用，前後端分離時需要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_todos(request: Request, db: Session = Depends(get_db)):
    todos = crud.get_todos(db)
    return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})

# 新增 todo
@app.post("/todos/")
async def create_todo(title: str = Form(...), db: Session = Depends(get_db)):
    todo = schemas.TodoCreate(title=title)
    crud.create_todo(db, todo)
    return RedirectResponse(url="/", status_code=303)

@app.post("/todos/{todo_id}/toggle")
async def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if todo:
        updated = schemas.TodoUpdate(completed=not todo.completed)
        crud.update_todo(db, todo_id, updated)
    return RedirectResponse(url="/", status_code=303)

@app.get("/todos/", response_model=list[schemas.TodoInDB])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.get("/todos/{todo_id}", response_model=schemas.TodoInDB)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.put("/todos/{todo_id}", response_model=schemas.TodoInDB)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return RedirectResponse(url="/", status_code=303)
