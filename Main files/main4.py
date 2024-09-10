from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from models4 import ShootingEvent

app = FastAPI()

# Sample JSON data
shooting_event_data = {
    "event": [
        {
            "id": "1",
            "name": "Pistol",
            "category": [
                {
                    "id": "10",
                    "name": "10 M Air Pistol",
                    "rounds": [
                        {
                            "id": "101",
                            "type": "Qualification",
                            "shots": 60,
                            "series": 6,
                            "isDecimal": False
                        },
                        {
                            "id": "102",
                            "type": "Finals",
                            "shots": 60,
                            "series": 6,
                            "isDecimal": False
                        }
                    ]
                },
                {
                    "id": "20",
                    "name": "25 metre standard pistol",
                    "rounds": [
                        {
                            "id": "201",
                            "type": "Qualification",
                            "shots": 60,
                            "series": 6,
                            "isDecimal": False
                        },
                        {
                            "id": "202",
                            "type": "Finals",
                            "shots": 120,
                            "series": 6,
                            "isDecimal": False
                        }
                    ]
                }
            ]
        },
        {
            "id": "2",
            "name": "Rifle",
            "category": [
                {
                    "id": "10",
                    "name": "10 M Air Rifle",
                    "rounds": [
                        {
                            "id": "101",
                            "type": "Qualification",
                            "shots": 60,
                            "series": 6,
                            "isDecimal": False
                        },
                        {
                            "id": "102",
                            "type": "Finals",
                            "shots": 60,
                            "series": 6,
                            "isDecimal": False
                        }
                    ]
                },
                {
                    "id": "20",
                    "name": "25 metre standard rifle",
                    "rounds": [
                        {
                            "id": "201",
                            "type": "Qualification",
                            "shots": 60,
                            "series": 6,
                            "isDecimal": False
                        },
                        {
                            "id": "202",
                            "type": "Finals",
                            "shots": 120,
                            "series": 6,
                            "isDecimal": False
                        }
                    ]
                }
            ]
        }
    ]
}

@app.get("/shooting_events", response_model=ShootingEvent)
async def get_shooting_events():
    return shooting_event_data
