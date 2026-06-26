from pydantic import BaseModel

this is the modification to check ne branch and merge with main branch
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False
    description: str = ""
    priority: int = 1
