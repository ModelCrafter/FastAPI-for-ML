"""
================================================================================
                    FastAPI Basics - Theoretical Introduction
================================================================================

Welcome to FastAPI! This document provides a comprehensive introduction to 
building modern, powerful REST APIs using FastAPI.

ASSUMPTION:
We assume you have a solid understanding of Python fundamentals. You should be 
comfortable with functions, decorators, and async/await syntax. If you are, 
you're ready to dive in!

================================================================================
                           WHAT IS FASTAPI?
================================================================================

FastAPI is a modern web framework for building APIs with Python. It's known for:
- Blazing speed: One of the fastest Python frameworks available
- Automatic data validation: Built-in validation using Pydantic models
- Interactive documentation: Auto-generated API docs with Swagger UI
- Type hints: Full type annotation support for better code quality
- Easy to learn: Intuitive API with minimal boilerplate code

REST APIs communicate using HTTP methods. Each method has a specific purpose 
in the CRUD (Create, Read, Update, Delete) cycle.

================================================================================
         THE FOUR FUNDAMENTAL HTTP METHODS (ENDPOINTS OVERVIEW)
================================================================================

── 1. GET REQUEST ──────────────────────────────────────────────────────────

Purpose: Retrieve data from the server
Characteristics:
  • Safe: Does not modify any data on the server
  • Idempotent: Can be called multiple times with the same result
  • No body: Data is passed through URL parameters (path or query)
  • Cacheable: Responses can be cached by browsers and proxies

Why use GET:
  • Fetch a list of users
  • Retrieve a specific product by ID
  • Get weather information
  • Search for results based on filters
  
Real-world analogy: GET is like asking someone to read information from a book 
without changing anything in the book. You're just extracting data.


── 2. POST REQUEST ────────────────────────────────────────────────────────

Purpose: Create new data on the server
Characteristics:
  • Not safe: Modifies data on the server by creating new resources
  • Not idempotent: Calling it multiple times creates multiple new resources
  • Includes body: Data is sent in the request body (usually JSON)
  • Not cacheable: Responses shouldn't be cached

Why use POST:
  • Create a new user account
  • Submit a form with user information
  • Upload a file to the server
  • Save a new blog post or comment
  
Real-world analogy: POST is like filling out a form and submitting it. Each 
submission creates something new on the server.


── 3. PUT REQUEST ─────────────────────────────────────────────────────────

Purpose: Update existing data on the server
Characteristics:
  • Not safe: Modifies data on the server by replacing resources
  • Idempotent: Calling it multiple times produces the same result
  • Includes body: Complete updated data is sent in the request body
  • Targets specific resource: You specify which resource to update via URL

Why use PUT:
  • Update a user's profile information
  • Modify an existing product listing
  • Replace an entire article or blog post
  • Update user settings or preferences
  
Real-world analogy: PUT is like replacing all the information on an index card 
with new information. The old data is completely replaced.


── 4. DELETE REQUEST ───────────────────────────────────────────────────────

Purpose: Remove data from the server
Characteristics:
  • Not safe: Removes data from the server permanently
  • Idempotent: Deleting the same resource multiple times has the same effect
  • No body (typically): The resource to delete is specified in the URL
  • Destructive: Operation cannot be easily undone

Why use DELETE:
  • Remove a user account
  • Delete a blog post or comment
  • Remove an item from inventory
  • Unsubscribe from a service
  
Real-world analogy: DELETE is like permanently removing an index card from a 
filing cabinet. Once it's gone, it's gone.


================================================================================
                    PRACTICAL DIFFERENCES EXPLAINED
================================================================================

URL vs Request Body:
  • GET requests: Data goes in the URL (path parameters or query strings)
  • POST/PUT requests: Data goes in the request body (JSON, form data, etc.)
  • DELETE requests: Resource location in URL, minimal or no body data

Idempotency (calling the same operation multiple times):
  • GET: Always returns the same data (idempotent)
  • POST: Creates new data each time (NOT idempotent - dangerous!)
  • PUT: Updates to the same state each time (idempotent)
  • DELETE: Same result each time (idempotent)

Safety (whether it modifies data):
  • GET: Safe - never modifies server data
  • POST: Not safe - creates new data
  • PUT: Not safe - modifies existing data
  • DELETE: Not safe - removes data

================================================================================
                     UNDERSTANDING PARAMETERS
================================================================================

Path Parameters:
  Format: /users/{user_id}
  Purpose: Part of the resource's address, always required
  Example: GET /users/123 (get user with ID 123)
  Use when: The value identifies which specific resource you're working with

Query Parameters:
  Format: /items/?skip=10&limit=5&search=python
  Purpose: Optional filters or options, appear after the ? in URL
  Example: GET /items/?skip=20&limit=10 (pagination)
  Use when: You need to filter, sort, or customize the response without 
            changing the endpoint's meaning

Request Body:
  Format: Sent as JSON or other formats in the request body
  Purpose: Contains data to create or update resources
  Example: POST /users/ with body: {"name": "John", "email": "john@example.com"}
  Use when: You need to send complex or sensitive data (POST/PUT)

================================================================================
                         KEY TAKEAWAYS
================================================================================

1. GET retrieves data without modifying anything
2. POST creates new resources and should not be repeated accidentally
3. PUT updates existing resources and is safe to repeat
4. DELETE removes resources permanently
5. Understanding HTTP methods prevents mistakes in API design
6. Path parameters are required, query parameters are optional filters
7. FastAPI automatically validates and converts types based on annotations

This foundation is essential for building robust, RESTful APIs!
"""\n








    


