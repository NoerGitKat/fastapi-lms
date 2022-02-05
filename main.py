from fastapi import FastAPI
from models.users_models import User

app = FastAPI()

# Temp
users= []

@app.get("/users")
async def get_users():
  return users

@app.post("/users/new")
async def create_user(new_user: User):
  users.append(new_user)
  return users