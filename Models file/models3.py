import datetime
from typing import Optional       # Optional is used to indicate that a value might not be present
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

# creating a relation between club and competetion  

class competetion_club(BaseModel):    #  class with relationship of competetion and club
    competetion_club_id: Optional [UUID] = uuid4()  # unique identifier for each cometetion club    
    competetion_id: UUID
    club_id: UUID

    
    
    # creating a relation between player and competetion

class competetion_player(BaseModel):    #  class with relationship of competetion and play
    competetion_player_id: Optional [UUID] = uuid4()  # unique identifier for each cometetion player
    competetion_id: UUID
    player_id: UUID

        












