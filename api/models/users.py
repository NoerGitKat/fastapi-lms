from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
  id: int
  email: str
  is_activated: bool
  bio: Optional[str]