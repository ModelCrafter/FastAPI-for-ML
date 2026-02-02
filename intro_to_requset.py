from fastapi import FastAPI, Request, Query

app = FastAPI()


@app.get("/debug")
async def debug(request: Request, query_param: int = Query(ge=0, le=100)):
    """
    Debug endpoint that returns detailed information about the incoming HTTP request.

    This asynchronous function extracts and returns key components of the request, such as the HTTP method,
    URL path, query parameters, and headers. It also accepts an optional query parameter 'query_param'
    which must be an integer between 0 and 100 (inclusive). If the parameter is out of range,
    FastAPI will automatically return a 422 Unprocessable Entity error.

    Parameters:
    - request (Request): The full HTTP request object, providing access to method, URL, headers, etc.
    - query_param (int): An optional query parameter with validation constraints (ge=0, le=100).
      Defaults to None if not provided, but validation ensures it's within range if present.

    Returns:
    - dict: A dictionary containing:
      - "method": The HTTP method (e.g., "GET").
      - "path": The URL path (e.g., "/debug").
      - "query": A dictionary of all query parameters.
      - "headers": A dictionary of all request headers.

    Example:
    - Request: GET /debug?query_param=50
    - Response: {
        "method": "GET",
        "path": "/debug",
        "query": {"query_param": "50"},
        "headers": {"host": "localhost:8000", ...}
      }
    - If query_param=150: Returns 422 error due to validation.
    """
    # Extract the HTTP method from the request (e.g., GET, POST)
    # This is useful for logging or conditional logic based on the request type.
    method = request.method

    # Extract the path from the URL (e.g., /debug)
    # Note: This excludes query parameters; use request.url for the full URL.
    path = request.url.path

    # Convert query parameters to a dictionary for easy access
    # request.query_params is a QueryParams object; dict() makes it a standard dict.
    query = dict(request.query_params)

    # Convert headers to a dictionary
    # request.headers is a Headers object; dict() converts it for JSON serialization.
    headers = dict(request.headers)

    # Return the extracted information in a structured dictionary
    # In a real application, you might filter sensitive headers or add authentication checks.
    return {
        "method": method,
        "path": path,
        "query": query,
        "headers": headers,
    }