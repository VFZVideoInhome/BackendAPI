from typing import List, Optional
from uuid import UUID, uuid4    # uuid4() generates a random UUID                                                                       
from pydantic import BaseModel, Field
from datetime import datetime   # datetime.datetime.now() generates current date and time
from models2 import player, address  # import competetion model  
from fastapi import FastAPI

app = FastAPI()

db:List[player] = [

    player(
        player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64d400"),
        player_firstname="Jitu",
        player_lastname="Rai", 
        player_dateofbirth="2023-06-06", 
        player_emailaddress="JituRai@gmail.com", 
        player_contactnumber="+918827530078", 
        player_address=address(
            address_street="Army Cantt Mhow", 
            address_housenumber="Army Cantt Mhow", 
            address_postcode="453441", 
            address_city="Mhow",
            address_country="India"
            ),
        player_clubname="AMU Mhow", 
        player_clubid="AMU001", 
        player_coachname="Army Coach", 
        player_coachid="Army Coach"
    ),
    
    player(

        player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64d500"),
        player_firstname="Swatantra",
        player_lastname="sohni", 
        player_dateofbirth="2023-10-10", 
        player_emailaddress="MeetuRai@gmail.com", 
        player_contactnumber="+918840030078", 
        player_address=address(
            address_street="Army Cantt Pune", 
            address_housenumber="171 sumatra", 
            address_postcode="493552", 
            address_city="pune",
            address_country="china"
            ),
        player_clubname="AMU Pune", 
        player_clubid="AMU002", 
        player_coachname="Dewashish", 
        player_coachid="Dewa Coach"
    ),
] # list of players



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/player")  # http://                                   
async def fetch_player():    # http://                   
    return db ;             # http:// """


@app.post("/api/v1/player")  # http://


async def register_player(player:player):    # http:// 
    db.append(player)                   # http://
    return {"id":player.player_id}                     # http://
                                            






















""" 
@app.get("/clubs/{club_id}")  # http://localhost:8000/clubs/1                           

async def fetch_club(club_id: UUID):    # http://localhost:8000/clubs/1                 
    for club in db:                     # http://localhost:8000/clubs/1                             
        if club.club_id == club_id:     # http://localhost:8000/clubs/1


            return club                 # http://localhost:8000/clubs/1




@app.post("/clubs")  # http://localhost:8000/clubs/1                    

async def create_club(club: club):    # http://localhost:8000/clubs/1
    club.club_id = uuid4()            # http://localhost:8000/clubs/1
    db.append(club)                   # http://localhost:8000/clubs/1

    return club                       # http://localhost:8000/clubs/1


@app.delete("/clubs/{club_id}")  # http://localhost:8000/clubs/1            


async def delete_club(club_id: UUID):    # http://localhost:8000/clubs/1
    for club in db:                      # http://localhost:8000/clubs/1
        if club.club_id == club_id:      # http://localhost:8000/clubs/1
            db.remove(club)              # http://localhost:8000/clubs/1    




@app.put("/clubs/{club_id}")  # http://localhost:8000/clubs/1


async def update_club(club_id: UUID, club: club):    # http://localhost:8000/clubs/1
    for club in db:                                  # http://localhost:8000/clubs/1

        if club.club_id == club_id:                  # http://localhost:8000/clubs/1


            club.club_name = club.club_name         # http://localhost:8000/clubs/1
            club.club_address = club.club_address   # http://localhost:8000/clubs/1


            club.club_YearOfEstablishment = club.club_YearOfEstablishment  # http://localhost:8000/clubs/1
            club.club_contact = club.club_contact                        # http://localhost:8000/clubs/1    




            club.club_email = club.club_email                            # http://localhost:8000/clubs/1


            club.club_OfficialID = club.club_OfficialID                  # http://localhost:8000/clubs/1    




            return club                                                  # http://localhost:8000/clubs/1        






















 """



















