# should install email-validator package
# pip install email-validator
from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


try:
    user = User(
        email='youssef@example.com',
        website='https://example.com'
    )

    print(user)
except ValidationError as e:
    print(e)

 
