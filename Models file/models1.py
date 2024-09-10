import datetime
from typing import Optional       # Optional is used to indicate that a value might not be present
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum



class competetion_type(str,Enum):    # list of competetion types like internal, national or international

 Internal  = "Internal"
 National  = "National" 
 International = "International"


class competetion(BaseModel):

    competetion_id: Optional [UUID] = uuid4()  # unique identifier for each cometetion                 
    competetion_name: str
    competetion_place: str
    competetion_date: datetime.datetime
    competetion_type: competetion_type  # list of competetion types like internal, national or international

    """ competetion_club: list  # list of clubs participating in the competetion
    competetion_organizer: str
    competetion_organizer_contact: str
    competetion_organizer_email: str
    competetion_organizer_OfficialID: str 
 """



