from typing import List

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Test(Base):
    __tablename__ = "test_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    test_int_param: Mapped[int]
    test_bool_param: Mapped[bool]
    test_str_param = Mapped[str]
    test_list_param = Mapped[List]
