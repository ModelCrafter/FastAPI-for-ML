from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()


# the status code:
# by default is 200 but can be changed

class post(BaseModel):
    title: str
    nb_views: int

@app.post('/posts', status_code=status.HTTP_201_CREATED) # also can write status_code=201 but from status is better
async def create_post(post: post):
    return post

# also when you used delete method ypu can set status code to 204 no content
@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    return {"message": f"post with id {id} has been deleted"}


dummy_db = {
    1: {"title": "first post", "nb_views": 10},
    2: {"title": "second post", "nb_views": 20},
}

# response model
# in this case we want to return only title not nb_views and imagine we have more fields in the db, end user does not need to see all fields
# so we create a response model that contains only the fields we want to return

class PostTitle(BaseModel):
    title: str


@app.get('/posts/{id}', response_model=PostTitle)
async def get_post(id: int):
    return dummy_db[id]


# now when we call this endpoint we will get only the title field in the response




