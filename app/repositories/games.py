from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Game

def get_all(db: Session) -> list[Game]:
    return db.scalars(
        select(Game)
    ).all()

def get_by_id(
        db: Session,
        game_id: int
) -> Game | None:
    return db.get(Game, game_id)

def create(
        db: Session,
        game: Game
) -> Game:
    db.add(game)
    db.commit()
    db.refresh(game)

    return game

def update(
        db: Session,
        game: Game
) -> Game:
    db.commit()
    db.refresh(game)

    return game

def delete(
        db: Session,
        game: Game
) -> None:
    db.delete(game)
    db.commit()