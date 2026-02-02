from fastapi import APIRouter, Response, HTTPException, Query, Path
from fastapi import status 
from typing import List
from first_project.schemes.user import UserIn, UserOut, UserType
from first_project.dummy_db import users


router = APIRouter()

@router.get('/users')
async def get_all_users() -> List[UserOut]:
    return list(users.values())



@router.get('/users/{user_id}', response_model=UserOut)
async def get_user_by_id( id: int = Query(ge=1)) -> UserOut:
    if id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users[id]



@router.post('/users/', response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user:UserIn) -> UserOut:
    new_id = max(users.keys()) + 1
    user_out = UserOut(id=new_id, user_type=user.user_type)
    users[new_id] = {'id': new_id, **user.dict()}
    return user_out



@router.put('/users/{user_id}', response_model=UserOut, status_code=status.HTTP_200_OK)
async def update_user(new_user: UserIn, user_id: int = Path(ge=1)) -> UserOut:
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    users[user_id] = {'id': user_id, **new_user.dict()}
    return UserOut(id=user_id, user_type=new_user.user_type)



@router.delete('/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int = Path(ge=1)) -> None:
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    del users[user_id]
    return None

