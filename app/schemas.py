from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str | None = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TodoInDB(TodoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
