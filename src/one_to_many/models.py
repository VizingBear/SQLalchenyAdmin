from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Parent(Base):
    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    name: Mapped[str]
