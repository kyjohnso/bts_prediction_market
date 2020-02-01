#!/usr/bin/env python
from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import players

app = FastAPI()
app.include_router(
    players.router,
    prefix="/players"
)
