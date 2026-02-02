# Import required libraries
from fastapi import FastAPI, Body, File, UploadFile
from enum import Enum
from pydantic import BaseModel
from typing import List

# Create FastAPI application instance
app = FastAPI()

# Function to create a user using direct Body parameters
@app.post('/users/')
async def create_user(name: str = Body(...), age: int = Body(...)) -> dict:
    """
    This function receives user data directly from the request body.
    - name: User's name, required.
    - age: User's age, required.
    Returns a dictionary with name and age.
    """
    return {"name": name, "age": age}

# Define User model using Pydantic
class User(BaseModel):
    name: str
    age: int

# Define enum for output format
class UserFormat(str, Enum):
    SHORT = "short"
    DETAILED = "detailed"

# Function to create a user using the model and output format
@app.post('/users/model/')
async def create_user_model(user: User, format: UserFormat) -> dict:
    """
    This function receives a user as a User object and an output format.
    - user: User object containing name and age.
    - format: Output format, either SHORT or DETAILED.
    If format is SHORT, returns only the name.
    Otherwise, returns the user and format.
    """
    if format == UserFormat.SHORT:
        return {"name": user.name}
    else:
        return {"user": user, "format": format}

# Another function to create a user with priority
@app.post('/users/create/')
async def create_user_with_priority(user: User, priority: int = Body(..., ge=0, le=4)) -> dict:
    """
    This function receives a user and priority from the body.
    - user: User object.
    - priority: Priority between 0 and 4, required from body.
    Returns the user and priority.
    """
    return {"user": user, "priority": priority}


# Function to upload a file and return its size - "body include file uploads"-
# but this approach is not recommended for large files because it loads the entire file into memory
@app.post('/files')
async def upload_file(file: bytes = File(...)) -> dict:
    return {"file_size": len(file)}


# Function to upload a file and return its size - recommended approach for large files
@app.post('/upload_large_file')
async def upload_large_file(file: UploadFile = File(...)) -> dict:
    return {"filename": file.filename, "content_type": file.content_type}  

@app.post('/multiupload_files')
async def multiupload(files: List[UploadFile] = File(...)) -> list:
    return [{"filename": file.filename} for file in files]

# Tips: if you put list class -built-in class- in swagger ui will get error 422 so you should use List from typing module or try endpoint by yourself with curl or httpie










