from pydantic import BaseModel, EmailStr
from typing import Optional

class PhotoCreateSchema(BaseModel):
    title = str
    description = Optional[str] = None 
    image = str 
