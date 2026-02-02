from fastapi import FastAPI, HttpException, status
from pydantic import BaseModel

dummy_db = {
    1:{"name": "Alice", "age": 30},
    2:{"name": "Bob", "age": 25},
    3:{"name": "Charlie", "age": 35}
}

app = FastAPI()

class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None


@app.get('/users')
async def get_all_users() -> list[dict]:
    return dummy_db.values()

@app.patch('/users/{user_id}', status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in dummy_db.keys():
        raise HttpException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    user = dummy_db[user_id]

    update_fields = user_update.model_dump(exclude_unset=True)
    user.update(update_fields)

    return user


'unset_&_patch'