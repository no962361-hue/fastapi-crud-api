from fastapi import FastAPI , Depends , HTTPException , Request
from pydantic import BaseModel
import asyncio

async def test():
    await asyncio.sleep(2)
    return "test completed"
app = FastAPI()

class User (BaseModel):
    name: str
    age: int
def comme_check ():
    return "dependecy work"

@app.get("/users")

def get_users (name : str = Depends(comme_check)):
    return { "users": ["Alice", "Bob", "Charlie"], "dependency": name}

@app.get("/user/{user_id}")
def get_home (user_id: int):
    if user_id != 5:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    return {"user": f"User with ID {user_id}"}

@app.middleware("http")
async def log_request(request: Request, call_next):
    print("Received request:")
    response = await call_next(request)
    print("Response sent:")
    return response