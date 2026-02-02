from pydantic import BaseModel, ValidationError, validator, root_validator


# ============================================================================
# CUSTOM VALIDATORS - Apply validation logic to individual fields
# ============================================================================
# The @validator decorator allows us to define custom validation rules for fields.
# This is useful for complex logic that goes beyond simple type checking.

class User(BaseModel):
    username: str

    # Validator for username: Ensures the username is at least 5 characters long
    # The @validator decorator intercepts the field value before it's assigned
    @validator('username')
    def username_must_be_big(cls, v: str):
        if len(v) < 5:
            raise ValueError('username must be at least 5 characters long')
        return v
    

# ============================================================================
# TESTING CUSTOM VALIDATOR
# ============================================================================
# This test demonstrates that validation fails when the username is too short

try:
    user = User(username='abc')
except ValidationError as e:
    print(e)


# ============================================================================
# MULTIPLE FIELD VALIDATORS
# ============================================================================
# We can add separate validators for different fields in the same model.
# Each validator is independent and applies only to its specified field.

class Product(BaseModel):
    name: str
    price: float

    # Validator for name: Ensures the product name is not empty or just whitespace
    @validator('name')
    def name_must_not_be_empty(cls, v: str):
        if not v or v.strip() == '':
            raise ValueError('name must not be empty')
        return v

    # Validator for price: Ensures the price is a positive number
    @validator('price')
    def price_must_be_positive(cls, v: float):
        if v <= 0:
            raise ValueError('price must be positive')
        return v


# ============================================================================
# TESTING MULTIPLE VALIDATORS
# ============================================================================
# This test demonstrates validation failures for both empty name and negative price
try:
    product = Product(name=' ', price=-10)
except ValidationError as e:
    print(e)


# ============================================================================
# ROOT VALIDATOR - Validate across multiple fields
# ============================================================================
# The @root_validator decorator allows validation that depends on multiple fields.
# It receives all field values and can perform complex cross-field validation logic.
# Use skip_on_failure=True to skip validation if any field already has an error.

class User(BaseModel):
    username: str
    password: str
    confirm_password: str

    # Root validator: Checks if password and confirm_password fields match
    # This validator receives all values and can compare multiple fields
    # Returns the values dictionary after validation (can also modify values here)
    @root_validator(skip_on_failure=True)
    def passwords_match(cls, values):
        pw = values.get('password')
        cpw = values.get('confirm_password')
        if pw != cpw:
            raise ValueError('passwords do not match')
        return values
    

# ============================================================================
# PRE AND POST PROCESSING VALIDATORS
# ============================================================================
# Pre-validators: Process data BEFORE validation (e.g., strip whitespace)
# Always-validators: Execute regardless of whether field is provided
# This is useful for data transformation and setting defaults

class Item(BaseModel):
    name: str
    description: str | None = None

    # Pre-validator: Strips whitespace from the name field BEFORE validation
    # pre=True means this runs before type validation
    @validator('name', pre=True)
    def name_must_be_stripped(cls, v: str):
        return v.strip()

    # Always-validator: Executes even if description is not provided
    # Sets a default description based on the item name if not supplied
    @validator('description', always=True)
    def set_default_description(cls, v: str | None, values):
        if v is None:
            return f'Description for {values.get("name")}'
        return v


# ============================================================================
# TESTING PRE AND ALWAYS VALIDATORS
# ============================================================================
# This demonstrates how pre-validators clean input and always-validators set defaults
item = Item(name='  Sample Item  ')
print(item)

