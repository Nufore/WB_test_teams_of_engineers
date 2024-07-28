from typing import Optional
from pydantic import BaseModel


class Team(BaseModel):
    name: Optional[str] = None


class TeamCreate(Team):
    name: str
