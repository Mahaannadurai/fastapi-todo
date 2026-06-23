from fastapi import APIRouter, HTTPException
from app.models import Todo

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

# In-memory storage (no database needed for this project)
todos = []


@router.get("/")
def get_todos():
    return todos


@router.post("/")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo


@router.get("/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Todo deleted"}

@router.patch("/{todo_id}/complete")
def complete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todo.completed = True
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
