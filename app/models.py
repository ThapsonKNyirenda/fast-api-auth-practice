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
         

class UserSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class config:
        schema_extra = {
            "example": {
                "id": 1,
                "fullname": "sampleuser",
                "email": "user@example.com",
                "password": "password123"
            }
        }
        
class UserLoginSchema(BaseModel):
    email: str = Field(default=None)
    password: str = Field(default=None)
    
    class config:
        schema_extra = {
            "example": {
                "email": "sampleuser",
                "password": "password123"
            }
        }