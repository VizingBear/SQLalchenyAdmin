from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    # password = Mapped[Text]
    #
    # def verify_password(self, password):
    #     pwhash = bcrypt.hashpw(password, self.password)
    #     return self.password == pwhash
