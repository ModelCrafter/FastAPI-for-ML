"""
==========================================================================
Pydantic Optional Fields and Default Values Module
==========================================================================

This module demonstrates how to work with optional fields and default values
in Pydantic models, including proper handling of dynamic defaults using
default_factory with Field().
==========================================================================
"""

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
import time


# ========== EXAMPLE 1: Basic Optional Fields with Default Values ==========
class User(BaseModel):
    """
    User model demonstrating optional fields and default values.
    
    Attributes:
        name (str): Required field - user's full name.
        nickname (str | None): Optional field - defaults to None if not provided.
        subscribed (bool): Optional field - defaults to False if not provided.
    
    Example:
        user = User(name="John")
        # Results in: name='John', nickname=None, subscribed=False
    """
    name: str
    nickname: str | None = None
    subscribed: bool = False



# ========== EXAMPLE 2: INCORRECT Way - Static Defaults for Dynamic Values ==========
# ⚠️ IMPORTANT: Do NOT use this pattern for time-dependent or dynamic defaults!

# What is a dynamic default value?
# A dynamic default value is computed at runtime, such as:
#   - Current timestamp (datetime.now())
#   - Random numbers
#   - Values that depend on other factors during object creation
#   - Values that change over time or between instances

class Event(BaseModel):
    """
    Event model demonstrating INCORRECT usage of dynamic defaults.
    
    ⚠️ WARNING: The timestamp field will have the SAME value for all instances
    because datetime.now() is evaluated only once when the class is defined,
    not each time an instance is created.
    """
    timestamp: datetime = datetime.now()


# Test to show the problem with this approach
e1 = Event()
time.sleep(1)  # Wait 1 second
e2 = Event()
print(e1.timestamp == e2.timestamp)  
# Output: True (both have the SAME timestamp - this is the problem!)
# This happens because datetime.now() is evaluated only once during class definition
print("Event example - Both timestamps are identical (INCORRECT):")
print(f"  e1.timestamp: {e1.timestamp}")
print(f"  e2.timestamp: {e2.timestamp}")
print()


# ========== EXAMPLE 3: Using Field() for Validation and Metadata ==========
# Field() is a powerful tool from Pydantic that provides:
#   - Additional validation rules (min/max length, numeric ranges, patterns, etc.)
#   - Metadata and documentation for fields
#   - Works similarly to FastAPI's path(), query(), and body() functions
#   - Enables advanced configuration of model attributes

class Person(BaseModel):
    """
    Person model demonstrating Field() usage with validation constraints.
    
    Field() allows you to:
    1. Set validation constraints (max_length, ge, le, etc.)
    2. Add metadata and descriptions for documentation
    3. Define required vs optional fields
    4. Set default values with factory functions
    
    Attributes:
        name (str): Required field with maximum length of 50 characters.
        age (int): Required field between 18 and 120 inclusive.
        city (str): Optional field with default value "Unknown" and max length 15.
    """
    # Required field with validation: name must not exceed 50 characters
    # The ... (Ellipsis) indicates this is a required field with no default value
    name: str = Field(..., max_length=50, description="User's full name (max 50 chars)")
    
    # Required field with range validation: age must be between 18 and 120
    # ge = greater than or equal, le = less than or equal
    # Other comparison options: gt (greater than), lt (less than)
    age: int = Field(..., ge=18, le=120, description="User's age (must be 18-120)")
    
    # Optional field with default value and validation constraint
    city: str = Field("Unknown", max_length=15, description="User's city (max 15 chars)")


# Testing Person model with various scenarios
print("=" * 60)
print("Person Model Validation Examples:")
print("=" * 60)

try:
    # Valid instance - all constraints satisfied
    p1 = Person(name="Alice", age=30, city="New York")
    print("✓ p1 created successfully:")
    print(f"  {p1}\n")

    # Valid instance - city uses default value
    p2 = Person(name="Bob", age=18)
    print("✓ p2 created successfully (city defaults to 'Unknown'):")
    print(f"  {p2}\n")

except ValidationError as e:
    # If validation fails (e.g., name too long, age out of range), error is caught
    print("✗ Validation Error:")
    print(e)


# ========== EXAMPLE 4: CORRECT Way - Dynamic Defaults with default_factory ==========
# ✓ CORRECT APPROACH: Use default_factory for time-dependent or computed defaults

class Meeting(BaseModel):
    """
    Meeting model demonstrating the CORRECT way to handle dynamic default values.
    
    By using default_factory parameter in Field(), each instance gets its own
    computed value at creation time, not at class definition time.
    
    Attributes:
        start_time (datetime): Optional field that defaults to the current time
                              when a Meeting instance is created. Each instance
                              gets its own unique timestamp.
    """
    # Correct usage: default_factory=datetime.now
    # This ensures datetime.now() is called EACH TIME an instance is created
    # NOT when the class is defined
    start_time: datetime = Field(
        default_factory=datetime.now,
        description="Meeting start time (defaults to current time if not provided)"
    )


# Test to show the correct behavior with default_factory
print("\n" + "=" * 60)
print("Meeting Model - CORRECT Dynamic Defaults:")
print("=" * 60)

m1 = Meeting()
print(f"✓ m1 created at: {m1.start_time}")

time.sleep(1)  # Wait 1 second

m2 = Meeting()
print(f"✓ m2 created at: {m2.start_time}")

# Check if timestamps are different
print(f"\nAre timestamps different? {m1.start_time != m2.start_time}")
print("✓ Each instance has its OWN timestamp (CORRECT behavior!)")
print(f"  m1.start_time: {m1.start_time}")
print(f"  m2.start_time: {m2.start_time}")
