from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.database import Base, engine
from app.routers import games
from app.services.exceptions import GameNotFoundError


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.exception_handler(GameNotFoundError)
async def game_not_found_handler(
    request: Request,
    exc: GameNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)}
    )

app.include_router(games.router)