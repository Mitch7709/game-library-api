from sqlalchemy.orm import Session

from app.models import Game
from app.repositories import games as game_repository
from app.schemas import GameCreate, GamePatch
from app.services.exceptions import GameNotFoundError

def get_all_games(db: Session) -> list[Game]:
    return game_repository.get_all(db)

def get_game(
        db: Session,
        game_id: int
) -> Game:
    game = game_repository.get_by_id(db, game_id)

    if game is None:
        raise GameNotFoundError(game_id)

    return game

def create_game(
        db: Session,
        game_data: GameCreate
) -> Game: 
    game = Game(
        title=game_data.title,
        genre=game_data.genre,
        developer=game_data.developer,
        release_year=game_data.release_year,
        completed=game_data.completed,
        rating=game_data.rating
    )

    return game_repository.create(db, game)

def update_game(
        db: Session,
        game: Game,
        game_data: GamePatch
) -> Game:
    updates = game_data.model_dump(exclude_unset=True)

    for field, value in updates.items():
        setattr(game, field, value)

    return game_repository.update(db, game)

def delete_game(
        db: Session,
        game: Game
) -> None:
    game_repository.delete(db, game)