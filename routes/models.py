from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from uuid import UUID


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"


class User(BaseModel):
    user_name: str
    user_email: EmailStr
    user_gender: Gender
    user_password: str


class UserAuth(BaseModel):
    user_email: EmailStr
    user_password: str


class Blog(BaseModel):
    user_id: Optional[UUID] = None
    blog_title: str
    blog_description: str