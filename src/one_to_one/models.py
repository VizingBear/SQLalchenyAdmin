from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Potato(Base):
    __tablename__ = "potato_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    box: Mapped["Box"] = relationship(back_populates="potato")


class Box(Base):
    __tablename__ = "box_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("potato_table.id"))
    potato: Mapped["Potato"] = relationship(back_populates="box")
