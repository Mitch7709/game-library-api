from sqlalchemy.orm import Session

from app.models import Game
from app.repositories import games as game_repository
from app.schemas import GameCreate, GameUpdate

def get_all_games(db: Session) -> list[Game]:
    return game_repository.get_all(db)

def get_game(
        db: Session,
        game_id: int
) -> Game | None:
    return game_repository.get_by_id(db, game_id)

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
        game_data: GameUpdate
) -> Game:
    game.title = game_data.title
    game.genre = game_data.genre
    game.developer = game_data.developer
    game.release_year = game_data.release_year
    game.completed = game_data.completed
    game.rating = game_data.rating

    return game_repository.update(db, game)


def delete_game(
        db: Session,
        game: Game
) -> None:
    game_repository.delete(db, game)