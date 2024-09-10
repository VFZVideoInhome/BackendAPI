from typing import List, Optional
from uuid import UUID, uuid4    # uuid4() generates a random UUID                                                                       
from pydantic import BaseModel, Field
from datetime import datetime   # datetime.datetime.now() generates current date and time
from models import club
from fastapi import FastAPI

from models1 import competetion
from models2 import address, player
from models3 import competetion_club
from models3 import competetion_player


app = FastAPI()

#main file for relation between club and competetion

clubdb:List[club] = [
    club(id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641234"), club_name="AMU Mhow", club_address="Army Cantt 1234", club_YearOfEstablishment="1982-01-01T00:00:00Z", club_contact="CO Saab", club_email="CO_Saab@gmail.com", club_OfficialID="AMU001"),
    club(id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec645678"), club_name="AMU Pune", club_address="Army Cantt 5678", club_YearOfEstablishment="1985-01-01T00:00:00Z", club_contact="Doosre Saab", club_email="Doosre_Saab@gmail.com", club_OfficialID="AMU002")
] # list of clubs

competetiondb:List[competetion] = [
    competetion(competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec647777"), competetion_name="AMU Champion", competetion_place="Army Cant Mhow", competetion_date="2023-06-06T00:00:00Z", competetion_type="Internal"),
    competetion(competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec648888"), competetion_name="BSF Champion", competetion_place="Shooting Academy Bhopal", competetion_date="2022-05-05T00:00:00Z", competetion_type="National"),
    competetion(competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec649999"), competetion_name="NRAI Championship", competetion_place="Shooting Academy Bhopal", competetion_date="2022-05-05T00:00:00Z", competetion_type="National"),
    competetion(competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec646666"), competetion_name="ISSF Championship", competetion_place="Shooting Academy Bhopal", competetion_date="2022-05-05T00:00:00Z", competetion_type="National")

] # list of competetions

clubcompetetiondb:List[competetion_club] = [

    competetion_club(competetion_club_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641111"), competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec647777"), club_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641234")),
    competetion_club(competetion_club_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec642121"), competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec648888"), club_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641234")),
    competetion_club(competetion_club_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641313"), competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec649999"), club_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec645678")),
    competetion_club(competetion_club_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641414"), competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec646666"), club_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec645678")),
  
] # list of competetion_club
                                


""" @app.get("/api/v1/club/{id}/competetions")  # get request giving club as input and getting competetions as output   
async def fetch_club_competetions(id: UUID):    # http://localhost:8000/clubs/1                                   
    for club in clubdb:                     # http://localhost:8000/clubs/1                             
        if club.id == id:     # http://localhost:8000/clubs/1
            for competetion in competetiondb:
                for clubcompetetion in clubcompetetiondb:
                    if clubcompetetion.clubid == club.id and clubcompetetion.competetionid == competetion.competetion_id:
                        return competetion """

         

@app.get("/api/v1/club/{id}/competetions")
async def fetch_club_competetions(id: UUID):
    for club_obj in clubdb:
        if club_obj.id == id:
            matched_competitions = []
            for clubcompetetion in clubcompetetiondb:
                if clubcompetetion.club_id == club_obj.id:
                    for competition in competetiondb:
                        if competition.competetion_id == clubcompetetion.competetion_id:
                            matched_competitions.append(competition)
            return matched_competitions
        

# main file for relation between player and competetion

playerdb:List[player] = [  # list of players
    player (
        player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64d400"),
        player_firstname="Jitu",
        player_lastname="Rai",
        player_dateofbirth="2023-06-06",
        player_emailaddress="Jitu@gmail.com",   
        player_contactnumber="+918827530078",
         player_address=address(  
            address_street="Army Cantt Mhow",
            address_housenumber="Army Cantt Mhow",
            address_postcode="453441",
            address_city="Mhow",
            address_country="India",
         ),   
        player_clubname="AMU Mhow",
        player_clubid="AMU001",
        player_coachname="Army Coach",
        player_coachid="Army Coach",
    
    ),
    player (
        player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64d500"),
        player_firstname="Swatantra",
        player_lastname="sohni",
        player_dateofbirth="2023-10-10",
        player_emailaddress="swat@gmail.com",
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
    )
 ] # list of players

playercompetetiondb:List[competetion_player] = [

    competetion_player(competetion_player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641111"), competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec647777"), player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64d400")),
    competetion_player(competetion_player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec642121"), competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec648888"), player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64d400")),
    competetion_player(competetion_player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641313"), competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec649999"), player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64d400")),
    competetion_player(competetion_player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec641414"), competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec646666"), player_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64d500")),

] # list of competetion_player

""" @app.get("/api/v1/player/{id}/competetions")
async def fetch_player_competetions(id: UUID):
    for player in playerdb:
        if player.player_id == id:
            for competetion in competetiondb:
                for playercompetetion in playercompetetiondb:
                    if playercompetetion.playerid == player.player_id and playercompetetion.competetionid == competetion.competetion_id:
                        return competetion """


@app.get("/api/v1/player/{id}/competetions")
async def fetch_player_competetions(id: UUID):
    for player_obj in playerdb:
        if player_obj.player_id == id:  # Update the attribute name to player_id
            matched_competitions = []
            for playercompetetion in playercompetetiondb:
                if playercompetetion.player_id == player_obj.player_id:  # Update the attribute name to player_id
                    for competition in competetiondb:
                        if competition.competetion_id == playercompetetion.competetion_id:
                            matched_competitions.append(competition)
            return matched_competitions

# just a comment to check git


# post method player-competition to save player competition data agains the competition id and player id    
@app.post("/api/v1/player/{id}/competetions")




async def create_player_competetion(id: UUID, competetion_id: UUID):
    for player in playerdb:
        if player.player_id == id:
            for competetion in competetiondb:
                if competetion.competetion_id == competetion_id:
                    playercompetetiondb.append(competetion_player(competetion_player_id=uuid4(), competetion_id=competetion_id, player_id=id))

                    return playercompetetiondb[-1]

















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



















