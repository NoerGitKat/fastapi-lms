from pydantic import BaseModel
from typing import Optional


class Course(BaseModel):
    id: int
    name: str
    desc: str
    max_attendees: Optional[int]
