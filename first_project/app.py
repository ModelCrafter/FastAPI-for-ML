from fastapi import FastAPI

from first_project.routers.users import router as users_router
from first_project.routers.items import router as items_router



app = FastAPI()


app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(items_router, prefix="/items", tags=["items"])

