from fastapi import FastAPI

app= FastAPI() 

@app.get("/")
def home():
    return {"message": "i love you soo much"}

@app.get("/users")
def users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.get("/user/{user_id}")
def user(user_id: int):
    return {"user": f"User with ID {user_id}"}

@app.get("/search")
def search(age: int):
    return {"search": f"Search results for age {age}"}


@app.post("/users")
def create_user(name:str,age :int ):
    return {"user": f"User created with name {name} and age {age}"}

@app.post ("/products")
def create_product(name : str , age :int , salary :int ):
    return {"product": f"Product created with name {name} and age {age} and salary {salary}"}