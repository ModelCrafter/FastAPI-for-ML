# This module demonstrates various response types in FastAPI, including HTML, plain text, redirects, and file serving.
# It showcases how to use different response classes to customize the output of API endpoints.
# FastAPI allows specifying response classes in route decorators to control the format and behavior of responses.
# This is useful for building APIs that need to return different content types based on the endpoint.

from fastapi import FastAPI 
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse
from pathlib import Path

# Notice the response classes imported from fastapi.responses
# These classes enable returning responses in specific formats:
# - HTMLResponse: For returning HTML content directly.
# - PlainTextResponse: For returning plain text.
# - RedirectResponse: For redirecting the client to another URL.
# - FileResponse: For serving files from the server.
# Other available response classes include JSONResponse, StreamingResponse, etc., which can be used similarly.

app = FastAPI()

# Define a GET endpoint at "/html" that returns an HTML response.
# The response_class=HTMLResponse ensures the response is treated as HTML by the client.
# This is useful for serving web pages or HTML snippets directly from the API.
@app.get("/html", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"

# Define a GET endpoint at "/text" that returns a plain text response.
# The response_class=PlainTextResponse specifies that the response should be plain text.
# This can be used for simple text-based APIs or debugging endpoints.
@app.get("/text", response_class=PlainTextResponse)
async def read_text():
    return "Hello World"

# Also available response classes:
# - JSONResponse: For returning JSON data (default for most endpoints).
# - RedirectResponse: For HTTP redirects.
# - FileResponse: For serving static files.
# - StreamingResponse: For streaming large responses or real-time data.
# You can use them similarly by specifying response_class in the route decorator.

# Define a GET endpoint at "/" that performs a redirect.
# The response_class=RedirectResponse indicates a redirect response.
# By default, RedirectResponse uses status code 307 (Temporary Redirect), but you can specify a different code like 302 (Found).
# This endpoint redirects users from the root URL to "/html", effectively making "/" an alias for "/html".
@app.get("/", response_class=RedirectResponse)
async def redirect_example():
    # Return a RedirectResponse to "/html" with status code 302 (Found).
    # This causes the client to make a new request to "/html".
    # Uncomment the line below for default 307 status code: return RedirectResponse(url="/html")
    return RedirectResponse(url="/html", status_code=302)

# This endpoint redirects to the /html endpoint when accessed.
# Visiting "/" will redirect to "/html" and display the HTML response.
# This is a common pattern for setting up default routes or aliases in web applications.

# Define a GET endpoint at "/get_file" that serves a file.
# FileResponse is used to return the contents of a file from the server.
# This is ideal for serving static assets like images, documents, or code files.
# Ensure the file path is correct and accessible; otherwise, it may raise a FileNotFoundError.
@app.get("/get_file", response_class=FileResponse)
async def get_file():
    # Specify the path to the file to be served.
    # Here, it's pointing to "intro_to_body.py" in the workspace directory.
    # FileResponse will handle reading and sending the file with appropriate headers.
    file_path = "/workspaces/FastAPI-for-ML/intro_to_body.py" 
    return FileResponse(file_path)


