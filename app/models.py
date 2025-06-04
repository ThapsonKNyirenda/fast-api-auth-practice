from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class PostSchema(BaseModel):
     id: int = Field(default=None)
     title: str = Field(default=None)
     content: str = Field(default=None)
     class config:
         schema_extra = {
             "example": {
                 "title": "Sample Post",
                 "content": "This is a sample post content."
             }
         }