import imp
from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    id: int
    active: bool
    age: int
    name: str=Field
    gender: str
    email: str

    class Config:
        orm_mode = True

class UserSchemaCreate(BaseModel):
    active: bool
    age: int
    name: str=Field
    gender: str
    email: str

    class Config:
        orm_mode = True

  