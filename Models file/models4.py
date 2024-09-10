

# creating a model for list of shooting events, categories and rounds

from typing import List
from pydantic import BaseModel

class Round(BaseModel):
    id: str
    type: str
    shots: int
    series: int
    isDecimal: bool

class Category(BaseModel):
    id: str
    name: str
    rounds: List[Round]

class Event(BaseModel):
    id: str
    name: str
    category: List[Category]

class ShootingEvent(BaseModel):
    event: List[Event]
