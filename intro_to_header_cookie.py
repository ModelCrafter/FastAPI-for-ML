# Import necessary modules from FastAPI
# FastAPI is a modern web framework for building APIs with Python, based on standard Python type hints.
# Header and Cookie are used to extract values from HTTP request headers and cookies respectively.
from fastapi import FastAPI, Header, Cookie

# Create an instance of the FastAPI application
# This is the main entry point for defining routes and handling requests.
app = FastAPI()

# Define a GET endpoint at the root path '/'
# This endpoint demonstrates how to extract a custom header named 'hello' from the request.
# The 'hello' parameter is required (indicated by '...'), meaning the request must include this header.
@app.get('/')
async def get_header(hello: str = Header(...)):
    """
    Retrieve and return the value of the 'hello' header from the HTTP request.

    This function is an asynchronous endpoint that expects a custom header called 'hello'.
    If the header is not provided, FastAPI will automatically return a 422 Unprocessable Entity error.

    Parameters:
    - hello (str): The value extracted from the 'hello' header in the request. It is required.

    Returns:
    - dict: A dictionary containing the 'hello' key with the header's value.

    Example:
    - Request: GET / with header 'hello: world'
    - Response: {"hello": "world"}
    """
    # Simply return the header value in a dictionary format
    # This is a basic response; in a real application, you might process or validate the value further.
    return {'hello': hello}

# Define another GET endpoint at '/users'
# This endpoint extracts the 'User-Agent' header, which is a standard HTTP header sent by browsers and clients.
# It is also required, so the request must include it.
@app.get('/users')
async def get_header(user_agent: str = Header(...)):
    """
    Retrieve and return the value of the 'User-Agent' header from the HTTP request.

    The 'User-Agent' header typically contains information about the client making the request,
    such as the browser type and version. This is useful for analytics or conditional responses.

    Parameters:
    - user_agent (str): The value extracted from the 'User-Agent' header. It is required.

    Returns:
    - dict: A dictionary with the 'user_agent' key holding the header's value.

    Example:
    - Request: GET /users with header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    - Response: {"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    """
    # Return the User-Agent value directly
    # Note: In production, you might want to parse or sanitize this value for security reasons.
    return {'user_agent': user_agent}

# Define a GET endpoint at '/first_cookie'
# This endpoint demonstrates extracting a cookie named 'hello' from the request.
# Unlike headers, cookies are optional here (default None), so if not present, it returns None.
@app.get('/first_cookie')
async def get_cookie(hello: str | None = Cookie(None)):
    """
    Retrieve and return the value of the 'hello' cookie from the HTTP request, if present.

    Cookies are small pieces of data stored on the client side and sent with requests.
    This function uses the 'Cookie' parameter to extract the 'hello' cookie. If the cookie is not set,
    it defaults to None, allowing the endpoint to handle missing cookies gracefully.

    Parameters:
    - hello (str | None): The value from the 'hello' cookie. Defaults to None if not provided.

    Returns:
    - dict: A dictionary with the 'hello' key, which may be None if the cookie is absent.

    Example:
    - Request: GET /first_cookie with cookie 'hello=world'
    - Response: {"hello": "world"}
    - If no cookie: {"hello": null}
    """
    # Check if the cookie is present; if not, it will be None
    # This allows for conditional logic, e.g., setting a default value or redirecting.
    return {'hello': hello}


