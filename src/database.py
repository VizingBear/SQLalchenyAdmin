from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///salaries.db", connect_args={"check_same_thread": False})
session_local = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = session_local()

    try:
        yield db
    finally:
        db.close()
