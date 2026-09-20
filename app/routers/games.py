from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import Game, GameCreate, GameUpdate
from app.services import games as game_service

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

@router.get("", response_model=list[Game])
def get_games(db: Session = Depends(get_db)):
    return game_service.get_all_games(db)

@router.get("/{game_id}", response_model=Game)
def get_game(
    game_id: int,
    db: Session = Depends(get_db)
):
    game = game_service.get_game(db, game_id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )
    
    return game

@router.post("", response_model=Game, status_code=status.HTTP_201_CREATED)
def create_game(
    game: GameCreate,
    db: Session = Depends(get_db)
):
    return game_service.create_game(db, game)

@router.put("/{game_id}", response_model=Game)
def update_game(
    game_id: int,
    game_data: GameUpdate,
    db: Session = Depends(get_db)
):
    game = game_service.get_game(db, game_id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return game_service.update_game(db, game, game_data)

@router.delete("/{game_id}")
def delete_game(
    game_id: int,
    db: Session = Depends(get_db)
):
    game = game_service.get_game(db, game_id)

    if game is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    game_service.delete_game(db, game)

    return {
        "message": "Game deleted successfully"
    }