from fastapi import FastAPI, HTTPException
from models.users_models import User
from typing import List

app = FastAPI()

# Temp
users= []

@app.get("/users", response_model=List[User])
async def get_users():
  return users

@app.post("/users/new")
async def create_user(new_user: User):
  users.append(new_user)
  return users

@app.get("/users/{id}")
async def get_user(id: int):
  for user in users:
    if user.id == id:
      return user
  raise HTTPException(404, f"Can't find user with id: {id}!")