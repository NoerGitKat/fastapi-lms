from pydantic import BaseModel
from typing import Optional


class Section(BaseModel):
    id: int
    name: str
    desc: str
    max_attendees: Optional[int]
