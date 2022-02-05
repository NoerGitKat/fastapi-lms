from fastapi import FastAPI, HTTPException, Path, Query
from models.users_models import User
from typing import List

app = FastAPI(
    title="LMS Backend",
    description="Here you'll find the endpoints to a CRUD backend for a Learning Management Systems",
    version="0.0.1",
    contact={"name": "Noer Is Amazing", "email": "noer@lightworksweb.nl"},
)

# Temp
users = []


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users/new")
async def create_user(new_user: User):
    users.append(new_user)
    return users


@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The ID of the user you want to get.", gt=0),
    q: str = Query(None, max_length=5),
):
    for user in users:
        if user.id == id:
            return {"user": user, "query": q}
    raise HTTPException(404, f"Can't find user with id: {id}!")
