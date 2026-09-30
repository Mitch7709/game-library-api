from unittest.mock import Mock, patch

import pytest
from sqlalchemy.orm import Session

from app.models import Game
from app.schemas import GameCreate, GamePatch
from app.services import games as game_service
from app.services.exceptions import GameNotFoundError

def test_get_game():
    db = Mock(spec=Session)

    expected_game = Game(
        id=1,
        title="Portal",
        genre="Puzzle",
        developer="Valve",
        release_year=2007,
        completed=False,
        rating=9.5
    )

    game_service.game_repository.get_by_id = Mock(
        return_value=expected_game
    )

    result = game_service.get_game(db, 1)

    assert result is expected_game

    game_service.game_repository.get_by_id.assert_called_once_with(db, 1)

def test_get_game_raises_when_game_not_found():
    db = Mock(spec=Session)

    with patch(
        "app.services.games.game_repository.get_by_id",
        return_value=None
    ):

        with pytest.raises(GameNotFoundError) as exc_info:
            game_service.get_game(db, 999)

    assert exc_info.value.game_id == 999

def test_create_game():
    db = Mock(spec=Session)

    game_data = GameCreate(
        title="Elden Ring",
        genre="Action RPG",
        developer="FromSoftware",
        release_year=2022,
        completed=False,
        rating=10
    )

    expected_game = Game(
        id=1,
        title="Elden Ring",
        genre="Action RPG",
        developer="FromSoftware",
        release_year=2022,
        completed=False,
        rating=10
    )

    game_service.game_repository.create = Mock(
        return_value = expected_game
    )

    result = game_service.create_game(db, game_data)

    assert result is expected_game

    created_game = (
        game_service.game_repository.create.call_args.args[1]
    )

    assert created_game.title == "Elden Ring"
    assert created_game.genre == "Action RPG"
    assert created_game.developer == "FromSoftware"
    assert created_game.release_year == 2022
    assert created_game.completed is False
    assert created_game.rating == 10

def test_update_game_only_changes_supplied_fields():
    db = Mock(spec=Session)

    game = Game(
        id=1,
        title="Halo",
        genre="First-Person Shooter",
        developer="Bungie",
        release_year=2001,
        completed=False,
        rating=9.0
    )

    patch = GamePatch(
        completed=True
    )

    game_service.game_repository.update = Mock(
        return_value=game
    )

    result = game_service.update_game(db, game, patch)

    assert result is game
    assert game.completed is True

    assert game.title == "Halo"
    assert game.genre == "First-Person Shooter"
    assert game.developer == "Bungie"
    assert game.release_year == 2001
    assert game.rating == 9.0

    game_service.game_repository.update.assert_called_once_with(db, game)

def test_update_game_can_clear_rating():
    db = Mock(spec=Session)

    game = Game(
        id=1,
        title="Portal",
        genre="Puzzle",
        developer="Valve",
        release_year=2007,
        completed=False,
        rating=9.5
    )

    patch = GamePatch(
        rating=None
    )

    game_service.game_repository.update = Mock(
        return_value=game
    )

    result = game_service.update_game(db, game, patch)

    assert result.rating is None

def test_delete_game():
    db = Mock(spec=Session)

    game = Game(
        id=1,
        title="Doom",
        genre="First-Person Shooter",
        developer="id Software",
        release_year=1993,
        completed=False,
        rating=9.0
    )

    game_service.game_repository.delete = Mock()

    result = game_service.delete_game(db, game)

    assert result is None

    game_service.game_repository.delete.assert_called_once_with(db, game)