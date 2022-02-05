from typing import List
from fastapi import APIRouter, HTTPException, Path, Query

from ..models.sections import Section

router = APIRouter()

# Temp
sections = []


@router.get("/sections", response_model=List[Section], tags=["Sections"])
async def get_sections():
    return sections


@router.post("/sections/new", tags=["Sections"])
async def create_section(new_section: Section):
    sections.append(new_section)
    return sections


@router.get("/sections/{id}", tags=["Sections"])
async def get_section(
    id: int = Path(..., description="The ID of the section you want to get.", gt=0),
    q: str = Query(None, max_length=5),
):
    for section in sections:
        if section.id == id:
            return {"section": section, "query": q}
    raise HTTPException(404, f"Can't find section with id: {id}!")
