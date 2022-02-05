from typing import List
from fastapi import APIRouter, HTTPException, Path, Query

from ..models.courses import Course

router = APIRouter()

# Temp
courses = []


@router.get("/courses", response_model=List[Course], tags=["Courses"])
async def get_courses():
    return courses


@router.post("/courses/new", tags=["Courses"])
async def create_course(new_course: Course):
    courses.append(new_course)
    return courses


@router.get("/courses/{id}", tags=["Courses"])
async def get_course(
    id: int = Path(..., description="The ID of the course you want to get.", gt=0),
    q: str = Query(None, max_length=5),
):
    for course in courses:
        if course.id == id:
            return {"course": course, "query": q}
    raise HTTPException(404, f"Can't find course with id: {id}!")
