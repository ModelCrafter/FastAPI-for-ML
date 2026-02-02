from pydantic import BaseModel

"""
Pydantic models showing how to use inheritance to reuse fields.

This file demonstrates common patterns:
- Separate input/output models (e.g. hide passwords in responses).
- Use a shared base model to avoid repeating common fields.
- Extend bases for create/update/DB representations.
"""


# Simple input model used when creating a user (contains password)
class UserIn(BaseModel):
    username: str
    password: str
    email: str


# Response model for users: do not expose the password
class UserOut(BaseModel):
    username: str
    email: str


# Shared base for user-related models. Put common fields here.
class UserBase(BaseModel):
    username: str
    email: str


# Input model that inherits common user fields and adds the password.
# This avoids repeating `username` and `email` declarations.
class UserInInherited(UserBase):
    password: str


# Output model inheriting the shared fields. No extra fields needed.
class UserOutInherited(UserBase):
    pass


"""
Post models showing common patterns:
- `PostBase` contains fields shared across several post models.
- `PostCreate` is used when creating a new post (requires content).
- `PostUpdate` is for partial/full updates and can include defaults.
- `PostInDB` represents how a post is stored (includes DB ids).
"""


class PostBase(BaseModel):
    # Title is common to all post representations
    title: str


class PostCreate(PostBase):
    # Fields required when creating a post
    content: str


class PostUpdate(PostBase):
    # Fields allowed/used when updating a post
    content: str
    published: bool = True


class PostInDB(PostBase):
    # Fields that exist only in the database representation
    id: int
    owner_id: int


# Example: a user response that also includes a list of posts.
# We reuse `UserOut` for user fields and add `posts`.
class UserWithPosts(UserOut):
    posts: list[PostBase] = []


# Using inheritance keeps models concise and avoids duplication.

# as we did before, sometimes we want input model and send another output model
class UserIn(BaseModel):
    username: str
    password: str
    email: str

class UserOut(BaseModel):
    username: str
    email: str

# we can use more efficiently inheritance to avoid code duplication
class UserBase(BaseModel):
    username: str
    email: str
    # here we can add more common fields, root to any user model

class UserInInherited(UserBase):
    password: str
    # when we inherit, we just add the specific fields
    #here we add password only for input model
    # so this file gave three fileds: username, email, password

class UserOutInherited(UserBase):
    # no additional fields for output model
    pass

