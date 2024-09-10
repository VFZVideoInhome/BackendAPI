from typing import List, Optional
from uuid import UUID, uuid4    # uuid4() generates a random UUID                                                                       
from pydantic import BaseModel, Field
from datetime import datetime   # datetime.datetime.now() generates current date and time
from models1 import competetion  # import competetion model  
from fastapi import FastAPI

app = FastAPI()

db:List[competetion] = [
    competetion(competetion_id=UUID("b62b0bfc-d799-41f1-980b-9aa3ec64da99"), competetion_name="AMU Champion", competetion_place="Army Cant Mhow", competetion_date="2023-06-06T00:00:00Z", competetion_type="Internal"),
    competetion(competetion_id=UUID("46ce0517-e4c9-402a-9952-4fdb32530b88"), competetion_name="NRAI National Championship", competetion_place="Shooting Academy Bhopal", competetion_date="2022-05-05T00:00:00Z", competetion_type="National")
] # list of competetions


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/competetion")  # http://                                   
async def fetch_competetion():    # http://                   
    return db ;             # http:// """


@app.post("/api/v1/competetion")  # http://


async def register_competetion(competetion: competetion):    # http:// 
    db.append(competetion)                   # http://
    return {"id":competetion.competetion_id}                     # http://
                                            






















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



















