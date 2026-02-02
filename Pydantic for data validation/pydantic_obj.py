from pydantic import BaseModel


# first we have a useful method to get a dictionary from a Pydantic object

class City(BaseModel):
    name: str
    country: str

class Person(BaseModel):
    name: str
    age: int
    city: City

'''
print("=== Pydantic Object to Dictionary ===")
city = City(name="New York", country="USA")
person = Person(name="John Doe", age=30, city=city)
person_dict = person.dict()
print(person_dict)

print("\n=== Accessing Nested Attributes ===")
print(f"Person's Name: {person.name}")
print(f"Person's City: {person.city.name}, {person.city.country}")
print(f"Person's Age: {person.age}")

print("\n=== Nested Attributes using `.dict()` ===")
print(f"Person's Name from dict: {person_dict['name']}")
print(f"Person's City from dict: {person_dict['city']['name']}, {person_dict['city']['country']}")

'''

# include and exclude parameters
city = City(name="New York", country="USA")
person = Person(name="John Doe", age=30, city=city)

print("\n=== Using include and exclude in model_dump() ===")
print("Including only name and city:")
print(person.model_dump(include={"name", "city"}))
print("Excluding age:")
print(person.model_dump(exclude={"age"}))
print("Excluding city.country:")
print(person.model_dump(exclude={"city": {"country"}}))
print("Including only city.name:")
print(person.model_dump(include={"city": {"name"}}))
# Note: In Pydantic v2, use model_dump() instead of dict()

 
# for mobilty, we can use the same method to convert back from dictionary to Pydantic object
person_data = {
    "name": "Jane Smith",
    "age": 25,
    "city": {
        "name": "Los Angeles",
        "country": "USA"
    }
}   
person_from_dict = Person.model_validate(person_data)
print("\n=== Dictionary to Pydantic Object ===")
print(person_from_dict)
# or simply
person_from_dict_simple = Person(**person_data)
print(person_from_dict_simple)
# this is usful when receiving data from external sources like APIs or user input 
# for example when we have PersonBase and we have PersonDB, and we need to add id in PersonDB, but we receive data only for PersonBase so by this way we can easily convert between them

print("\n=== Creating Pydantic Object from Partial Data ===")
class PersonBase(BaseModel):
    name: str
    age: int

class PersonDB(PersonBase):
    id: int

base_data = {
    "name": "Alice Johnson",
    "age": 28
}
person_base = PersonBase(**base_data)
person_db = PersonDB(id=1 ,**person_base.model_dump())

print(person_db)


# also we can define functions in model to get dictionary representation with custom logic
class Product(BaseModel):
    id: int
    name: str
    price: float

    def get_only_name_id(self) -> dict:

        return self.model_dump(include={'name', 'id'})

        # return {"name": self.name, "id": self.id} 

    def to_dict_with_tax(self, tax_rate: float) -> dict:
        data = self.model_dump()
        data['price_with_tax'] = self.price * (1 + tax_rate)
        return data

product = Product(id=101, name="Laptop", price=999.99)
print("\n=== Custom Dictionary Representations ===")
print("Only Name and ID:")
print(product.get_only_name_id())
print("With Tax (10%):")
print(product.to_dict_with_tax(0.10))

# these methods are useful when we want to have different views of the same data model based on context

# let's go to unset parameter in include/exclude
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

item = Item(name="Book", price=12.99)
print("\n=== Using exclude_unset in model_dump() ===")
print("Without exclude_unset:")
print(item.model_dump())
print("With exclude_unset:")
print(item.model_dump(exclude_unset=True))

# we will demonstrate how to use exlude_unset with patch endpoint in FastAPI in anouther file 
# this is useful when we want to serialize only the fields that have been explicitly set by the user, ignoring default values