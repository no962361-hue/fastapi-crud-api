from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends
from fastapi import HTTPException


def get_home (user_id: int):
    if user_id < 0:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    return {"user": f"User with ID {user_id}"}