import datetime
from typing import Optional       # Optional is used to indicate that a value might not be present
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

# creating a model file for player
# replacing competetion with player in this file



class address(BaseModel):    # list of player address attributes

    address_street: str

    address_housenumber: str 

    address_postcode: str

    address_city: str

    address_country: str


class player(BaseModel):   # creating a model file for players


    player_id: Optional [UUID] = uuid4()  # unique identifier for each cometetion                 
    player_firstname: str
    player_lastname: str
    player_dateofbirth: datetime.date
    player_emailaddress: str
    player_contactnumber: str
    player_address: address
    player_clubname: str
    player_clubid: str
    player_coachname: str
    player_coachid: str


    """ player_club: list  # list of clubs participating in the player
    player_organizer: str
    player_organizer_contact: str
    player_organizer_email: str
    player_organizer_OfficialID: str 
 """



