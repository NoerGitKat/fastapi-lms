from typing import List
from fastapi import APIRouter, HTTPException, Path, Query

from ..models.users import User

router = APIRouter()

# Temp
users = []


@router.get("/users", response_model=List[User], tags=["Users"])
async def get_users():
    return users


@router.post("/users/new", tags=["Users"])
async def create_user(new_user: User):
    users.append(new_user)
    return users


@router.get("/users/{id}", tags=["Users"])
async def get_user(
    id: int = Path(..., description="The ID of the user you want to get.", gt=0),
    q: str = Query(None, max_length=5),
):
    for user in users:
        if user.id == id:
            return {"user": user, "query": q}
    raise HTTPException(404, f"Can't find user with id: {id}!")
