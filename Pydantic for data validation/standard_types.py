from pydantic import BaseModel, ValidationError
from enum import Enum
from datetime import date

# simple base model example

class Person(BaseModel):
    """Simple Person model with a name and an age.

    - `name`: person's full name as a string.
    - `age`: person's age as an integer.

    Pydantic will validate and coerce these fields on instantiation.
    """
    name: str  # person's full name as a string
    age: int   # person's age as an integer


#-----------------------------------------------------
# let's make it more complex with enum 

class Gender(str, Enum):
    """Enumeration for allowed gender values.

    Inherits from `str` so enum values behave like native strings
    (useful for JSON serialization and comparisons).
    Allowed values: 'male', 'female'.
    """
    MALE = 'male'
    FEMALE = 'female'

class Person(BaseModel):
        """Person model including a `gender` field.

        - `gender`: must be a member of the `Gender` enum (or a matching string).
            Pydantic will convert matching strings into the enum automatically.
        """
        name: str
        age: int
        gender : Gender  # must be one of Gender.MALE or Gender.FEMALE

try:
    person = Person(name='Alice', age=30, gender='non-binary') # This will raise a validation error because 'non-binary' is not a valid Gender
    print(person)
except ValidationError as e:
    #print(e) # uncomment to see validation error
    pass


#-----------------------------------------------------
# adding date field

class Person(BaseModel):
        """Person model extended with a `birth_date` field.

        - `birth_date` is a `datetime.date`. Pydantic accepts ISO-formatted
            date strings (e.g. '1998-11-01') and will coerce them to `date`.
        """
        name: str
        age: int
        gender : Gender
        birth_date: date  # ISO date (YYYY-MM-DD) or a `datetime.date` instance

try:
    person = Person(name='Bob', age=25, gender='male', birth_date='1998-13-01') # This will raise a validation error because the date is invalid
    print(person)
except ValidationError as e:
    #print(e)  # uncomment to see validation error
    pass  

try:
    person = Person(name='Bob', age=25, gender='male', birth_date='1998-11-01') # This will work correctly
    #print(person) # uncomment to see the valid person
except ValidationError as e:
    print(e)     


#-----------------------------------------------------
# nested models

class Address(BaseModel):
    """Simple nested Address model.

    - `street`: street address as a string.
    - `city`: city name as a string.
    This model can be passed as an `Address` instance or as a dict;
    Pydantic will construct it from a dict automatically.
    """
    street: str  # street address
    city: str    # city name

class Person(BaseModel):
        """Full Person model including a nested `Address`.

        - `address` is of type `Address` (a nested Pydantic model).
            You may pass an `Address` instance or a dict with the required
            address fields; Pydantic will parse it into `Address` automatically.
        """
        name: str
        age: int
        gender : Gender
        birth_date: date
        address: Address  # nested Address model


try:
    person = Person(
        name='Charlie', 
        age=40,
        gender='male',
        birth_date='1983-07-15',
        address=Address(street='123 Main St') # This will raise a validation error because city is missing
    )
    print(person)
except ValidationError as e:
    #print(e) # uncomment to see validation error
    pass


try:
    person = Person(
        name='Charlie', 
        age=40,
        gender='male',
        birth_date='1983-07-15',
        address=Address(street='123 Main St', city='New York') # This will work correctly
    )
    #print(person)
except ValidationError as e:
    print(e)
    

