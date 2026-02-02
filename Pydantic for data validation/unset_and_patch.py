"""
Module notes (added comments):

What PATCH means (simple, organized explanation):
- PATCH is an HTTP method intended for partial updates of a resource.
- With PATCH the client sends only the fields it wants to change. The server
    merges those changes into the existing resource.

What PUT means (simple):
- PUT is an HTTP method typically used to replace a resource with a new
    representation. The client usually sends the full resource.

Key differences between PATCH and PUT:
- Scope: PATCH = partial update; PUT = full replacement (commonly).
- Idempotency: PUT is idempotent (repeating the same request yields the
    same result). PATCH may or may not be idempotent depending on semantics.
- Typical use-cases: PATCH to change one or two fields; PUT to replace the
    whole object.

How this code uses PATCH:
- The `UserUpdate` model defines optional fields (they default to None).
- In `update_user` we call `user_update.model_dump(exclude_unset=True)` which
    returns only the fields the client actually sent in the request. This
    produces a dictionary of updates which we then apply to the stored user
    using `dict.update()` — leaving unspecified fields unchanged.

Example behaviours:
- PATCH /users/1 with body {"age": 31} -> only `age` is updated.
- PUT /users/1 with body {"name": "Alice"} -> may replace the full
    resource (`age` could be removed if omitted) depending on implementation.


"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

dummy_db = {
        1: {"name": "Alice", "age": 30},
        2: {"name": "Bob", "age": 25},
        3: {"name": "Charlie", "age": 35}
}

app = FastAPI()


class UserUpdate(BaseModel):
        # Optional fields: client may send none, one, or both fields.
        # Using optional fields fits PATCH semantics because we only want to
        # update the fields that are present in the request body.
        name: str | None = None
        age: int | None = None


@app.get('/users')
async def get_all_users() -> list[dict]:
        # Return a plain list so the JSON response is a JSON array.
        return list(dummy_db.values())


@app.patch('/users/{user_id}', status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user_update: UserUpdate):
        # If the user does not exist, respond with 404 Not Found.
        if user_id not in dummy_db.keys():
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        user = dummy_db[user_id]

        # `model_dump(exclude_unset=True)` returns only the fields the client
        # provided in the request. This is the core of partial-update (PATCH).
        update_fields = user_update.model_dump(exclude_unset=True)

        # Apply the provided changes to the stored user dict. Unspecified
        # fields remain untouched.
        user.update(update_fields)

        return user
