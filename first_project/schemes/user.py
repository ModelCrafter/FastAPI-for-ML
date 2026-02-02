from pydantic import BaseModel
from enum import Enum

class UserType(str, Enum):
    ADMIN = 'Admin'
    CUSTOMER = 'Customer'

class UserIn(BaseModel):
    name: str
    user_type: UserType

class UserOut(BaseModel):
    id: int
    user_type: UserType