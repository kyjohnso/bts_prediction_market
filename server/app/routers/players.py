#!/usr/bin/env python
from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["players"])
async def return_all_players():
    return [{"name": "Foo", "stats": [1, 2, 3]}, {"name": "Bar", "stats": [1, 2, 3]}]


@router.get("/players/{playername}", tags=["players"])
async def return_player_info(playername: str):
    return {"playername": playername, "stats": [1, 2, 3]}
