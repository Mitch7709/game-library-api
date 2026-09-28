from pydantic import BaseModel, Field

class GameCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    genre: str = Field(min_length=1, max_length=100)
    developer: str = Field(min_length=1, max_length=200)
    release_year: int = Field(ge=1950)
    completed: bool = False
    rating: float | None = Field(default=None, ge=0, le=10)

class GamePatch(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    genre: str | None = Field(default=None, min_length=1, max_length=100)
    developer: str | None = Field(default=None, min_length=1, max_length=200)
    release_year: int | None = Field(default=None, ge=1950)
    completed: bool | None = None
    rating: float | None = Field(default=None, ge=0, le=10)

class Game(GameCreate):
    id: int