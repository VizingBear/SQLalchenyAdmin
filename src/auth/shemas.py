from pydantic import BaseModel


class User_shema(BaseModel):
    name: str
    fullname: str
    # password: Text
