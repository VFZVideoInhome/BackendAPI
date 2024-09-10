import datetime
from typing import Optional       # Optional is used to indicate that a value might not be present
from uuid import UUID, uuid4
from pydantic import BaseModel


class club(BaseModel):

    id: Optional [UUID] = uuid4()  # unique identifier for each club                   
    club_name: str
    club_address: str
    club_YearOfEstablishment: datetime.datetime
    club_contact: str
    club_email: str
    club_OfficialID: str



    """ competetion_club: list  # list of clubs participating in the competetion
    competetion_organizer: str
    competetion_organizer_contact: str
    competetion_organizer_email: str
    competetion_organizer_OfficialID: str 
 """



