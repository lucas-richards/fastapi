from pydantic import BaseModel
import datetime


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    # enable id = data.id (not only data["id"])
    # acts as populate as well
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
    created_at: datetime.datetime

    class Config:
        from_attributes = True # renamed from orm_mode?