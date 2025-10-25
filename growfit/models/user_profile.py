from pydantic import BaseModel

class UserProfile(BaseModel):
    edad: int
    peso: float
    altura: float
