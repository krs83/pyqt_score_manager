from datetime import datetime

from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from db import Base


class Tournament(Base):
    __tablename__ = "tournaments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    categories: Mapped[list["Category"]] = relationship(back_populates="tournament")

    def __repr__(self):
        return f"<Tournament(id={self.id}, name={self.name})>"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tournament_id: Mapped[int] = mapped_column(Integer, ForeignKey("tournaments.id"))
    name: Mapped[str] = mapped_column(String(100))
    format: Mapped[str] = mapped_column(String(100))
    size: Mapped[int] = mapped_column(Integer)

    tournament: Mapped["Tournament"] = relationship(back_populates="categories")
    participants: Mapped[list["Participant"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    name: Mapped[str] = mapped_column(String(100))  # Assuming a maximum length of 100 characters for the name
    place: Mapped[int] = mapped_column(Integer, nullable=True)

    category: Mapped["Category"] = relationship(back_populates="participants")

    def __repr__(self):
        return f"<Participant(id={self.id}, name={self.name})>"


class Fight(Base):
    __tablename__ = "fights"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    round_number: Mapped[int] = mapped_column(Integer)
    slot_number: Mapped[int] = mapped_column(Integer)
    red_id: Mapped[int] = mapped_column(Integer, ForeignKey("participants.id"), nullable=True)
    blue_id: Mapped[int] = mapped_column(Integer, ForeignKey("participants.id"), nullable=True)
    winner_id: Mapped[int] = mapped_column(Integer, ForeignKey("participants.id"), nullable=True)
    red_score: Mapped[int] = mapped_column(Integer, default=0)
    red_adv: Mapped[int] = mapped_column(Integer, default=0)
    red_pen: Mapped[int] = mapped_column(Integer, default=0)
    blue_score: Mapped[int] = mapped_column(Integer, default=0)
    blue_adv: Mapped[int] = mapped_column(Integer, default=0)
    blue_pen: Mapped[int] = mapped_column(Integer, default=0)
    is_finished: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f"<Fight(id={self.id}, round_number={self.round_number}, slot_number={self.slot_number})>"
