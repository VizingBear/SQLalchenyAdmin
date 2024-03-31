from typing import List

from pydantic import BaseModel


class test_shemas(BaseModel):
    test_int_param: int
    test_bool_param: bool
    test_str_param: str
    test_list_param: List | None
