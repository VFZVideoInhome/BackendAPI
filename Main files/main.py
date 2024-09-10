from typing import List, Optional
from uuid import UUID, uuid4    # uuid4() generates a random UUID                                                                       
from pydantic import BaseModel, Field
from datetime import datetime   # datetime.datetime.now() generates current date and time
from models import club
from fastapi import FastAPI

app = FastAPI()

db:List[club] = [
    club(id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64dafe"), club_name="AMU Mhow", club_address="Army Cantt Mhow", club_YearOfEstablishment="1982-01-01T00:00:00Z", club_contact="CO Saab", club_email="CO_Saab@gmail.com", club_OfficialID="AMU001"),
    club(id=UUID("46ce0517-e4c9-402a-9952-4fdb32530b77"), club_name="AMU Pune", club_address="Army Cantt Pune", club_YearOfEstablishment="1985-01-01T00:00:00Z", club_contact="Doosre Saab", club_email="Doosre_Saab@gmail.com", club_OfficialID="AMU002")
] # list of clubs


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/club")  # http://                                   
async def fetch_clubs():    # http://                   
    return db ;             # http:// """

@app.post("/api/v1/club")  # http://


async def register_club(club: club):    # http://               
    db.append(club)                   # http://
    return {"id":club.id}                     # http://
        


""" @app.post("/api/v1/club")  # http://


async def register_club(club: club):    # http:// 
    db.append(club)                   # http://
    return {"id":club.id}                     # http://
                                             """






















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



















