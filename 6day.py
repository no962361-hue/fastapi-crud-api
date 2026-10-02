from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    id:int
    name:str
    age:int
    salary:int

users = []

@app.post("/users")
def create_user(new_user: user):
    users.append(new_user)
    return new_user

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
           return user
    return {"error": "User not found"}


@app.put("/users/{user_id}")
def update_user(user_id:int,updated_user:user):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return updated_user
    return {"error": "User not found"}

class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    salary: int | None = None

@app.patch("/users/{user_id}")
def update_user_partial(user_id:int, updated_user:UserUpdate):
    for  user in users:
        if user.id == user_id:
            if updated_user.name is not None:
                user.name = updated_user.name
            if updated_user.age is not None:
                user.age = updated_user.age
            if updated_user.salary is not None:
                user.salary = updated_user.salary
            return user
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": "User deleted"}

    return {"message": "User not found"}