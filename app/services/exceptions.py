class GameNotFoundError(Exception):
    def __init__(self, game_id: int):
        self.game_id = game_id
        super().__init__(f"Game with id {game_id} was not found")