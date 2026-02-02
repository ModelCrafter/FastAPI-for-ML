# Path Parameters in FastAPI
# This file demonstrates how to use path parameters in FastAPI endpoints.
# Path parameters are parts of the URL that are dynamic and can be extracted as variables.

from fastapi import FastAPI, Path
from enum import Enum

# Create a FastAPI application instance
app = FastAPI()

# Basic path parameters example
# This endpoint accepts two path parameters: 'type' as a string and 'id' as an integer
@app.get('items/{type}/{id}')
async def get_item(type: str, id: int):
    """
    Retrieve an item based on its type and ID.

    This function demonstrates basic path parameter usage in FastAPI.
    The URL path /items/{type}/{id} allows dynamic values for 'type' and 'id'.

    Args:
        type (str): The type of the item (e.g., 'book', 'movie').
        id (int): The unique identifier of the item.

    Returns:
        dict: A json containing the 'type' and 'id' of the item.
    """
    return {'type': type, 'id': id}

# Define enums for better type safety and validation
class UserType(str, Enum):
    """Enumeration for user types."""
    STANDARD = "standard"
    ADMIN = "admin"

class SID(int, Enum):
    """Enumeration for specific IDs."""
    ONE = 1
    HUNDRED = 100
    THOUSAND = 1000

# Path parameters with enums
# This endpoint uses enums to restrict the possible values for path parameters
@app.get('/users/type/{usertype}')
async def get_user_by_type(usertype: UserType, id: SID):
    """
    Retrieve a user based on their type and a specific ID.

    This function uses Enum types for path parameters to ensure only predefined
    values are accepted, providing better validation and type safety.

    Args:
        usertype (UserType): The type of the user (STANDARD or ADMIN).
        id (SID): A specific ID value (ONE, HUNDRED, or THOUSAND).

    Returns:
        dict: A dictionary containing the 'usertype' and 'id'.
    """
    return {'type': usertype, 'id': id}

# Path parameter with validation using Path
# This endpoint demonstrates advanced path parameter validation
@app.get('/license/{prem}')
async def get_license(prem: str = Path(
    ...,
    min_length=5,
    max_length=15,
    pattern=r"^\w{2}-\d{3}-\w{2}$",
    description="The license code in format XX-123-XX"
)):
    """
    Retrieve license information based on the premium code.

    This function uses FastAPI's Path parameter with validation constraints
    to ensure the license code follows a specific format.

    Args:
        prem (str): The license code, must be in format XX-123-XX (e.g., AB-456-CD).
                   Length between 5 and 15 characters, matching the regex pattern.

    Returns:
        dict: A dictionary containing the 'prem' license code.
    """
    return {'prem': prem}

# Path parameter with metadata
# This endpoint shows how to add title, description, and deprecation info
@app.get('/users/{id}')
async def get_user(id: int = Path(
    ...,
    title="User ID",
    description="The ID of the user",
    deprecated=True
)):
    """
    Retrieve a user by their ID.

    This function demonstrates how to add metadata to path parameters,
    including title, description, and deprecation status.

    Note: This endpoint is marked as deprecated.

    Args:
        id (int): The unique identifier of the user.

    Returns:
        dict: A dictionary containing the 'id' of the user.
    """
    return {'id': id}

# Note: The following are common validation operators for Path parameters:
# gt : greater than
# ge : greater than or equal to
# lt : less than
# le : less than or equal to
# These can be used in Path(...) for numeric validations, e.g., Path(..., gt=0)


