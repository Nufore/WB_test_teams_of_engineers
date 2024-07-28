from pydantic import BaseModel
from typing import Optional


class Engineer(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class EngineerCreate(Engineer):
    first_name: str
    last_name: str


class EngineerPatch(Engineer):
    team_id: Optional[int] = None


class EngineerPut(EngineerCreate):
    team_id: int
