from fastapi import FastAPI, Response, status, HTTPException, Body


app = FastAPI()
# Example endpoint demonstrating custom response with specific headers



@app.get("/custom-response/")
async def custom_response(response: Response):
    response.headers["X-Custom-Header"] = "CustomValue"
    return {"message": "This is a custom response"}


# Example setting a cookie in the response
@app.get("/set-cookie/")
async def set_cookie(response: Response):
    response.set_cookie(key="my_cookie", value="cookie_value", max_age=86400)  # Cookie valid for 30 minutes
    return {"message": "Cookie has been set"}


# Example Dynamic status Code
@app.get("/dynamic-status/{page}")
async def dynamic_status(page: int, response: Response):
    if page != 1:
        response.status_code = status.HTTP_201_CREATED

    return {"pages": page}

 # when we call this funvction with page other than 1 it will return status code 201
 # and for page 1 it will return status code 200




# simple Raiseing HTTP Exceptions with custom status codes
@app.post("/raise-exception/")
async def get_password(password: str = Body(...)):
    if len(password) < 8:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail = 'password must be at least 8 characters long')
    
    return {'message': 'Password is valid'}


# what if we want to put more hints in the exception
@app.post("/detailed-exception/")
async def detailed_exception(password: str = Body(...)):
    if len(password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 8 characters long",
            headers={"X-Error": "Invalid Password Length"},
        )
    
    return {'message': 'Password is valid'}


# also we can give end user structured error info
@app.post("/structured-exception/")
async def structured_exception( password: str = Body(...)):
    if len(password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "Invalid Password",
                "message": "Password must be at least 8 characters long",
                "code": '400 Bad Request'
            },
        )
    
    return {'message': 'Password is valid'}


    
    

    

