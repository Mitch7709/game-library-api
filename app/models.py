from sqlalchemy import Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    genre: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    developer: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    release_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    rating: Mapped[float | None] = mapped_column(
        nullable=True
    )