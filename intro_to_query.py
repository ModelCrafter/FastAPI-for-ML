# Import required libraries for creating FastAPI app and defining queries
from fastapi import FastAPI, Query
from enum import Enum

# Create an instance of FastAPI app to handle requests and responses
app = FastAPI()

# Define an Enum to specify user display formats: short or detailed
class UserFormat(str, Enum):
    SHORT = "short"      # Short format
    DETAILED = "detailed"  # Detailed format

# Endpoint to get page information and required data size
@app.get('/users_size/')
async def get_users_size(page: int = 0, size: int = 10):
    """
    Function to return the page number and data size.
    - page: Default page number is 0
    - size: Default data size is 10
    Returns a dictionary containing the specified values.
    """
    # Return the values as a dictionary
    return {'page': page, 'size': size}

# Endpoint to get the user display format
@app.get('/users/format/')
async def get_users_format(format: UserFormat):
    """
    Function to return the specified format for displaying users.
    - format: Value from UserFormat Enum (short or detailed)
    Returns a dictionary containing the format.
    """
    # Return the format as a dictionary
    return {'format': format}

# Endpoint to get age with value validation
@app.get('/users_age/')
async def get_age(age: int = Query(18, ge=18, le=120)):
    """
    Function to return age with validation that it is between 18 and 120.
    - age: Default age is 18, must be >=18 and <=120
    Uses Query for validation.
    Returns a dictionary containing the age.
    """
    # Return the age as a dictionary after validation
    return {'age': age}


