from pydantic import BaseModel

class User(BaseModel):
  email: str
  is_activated: str