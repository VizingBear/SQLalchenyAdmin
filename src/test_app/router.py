from typing import Annotated, Union

from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/items/")
async def read_items(
        q: Annotated[
            Union[str, None],
            Query(
                alias="item-query",
                title="Query string",
                description="Query string for the items to search in the database that have a good match",
                min_length=3,
                max_length=50,
            ),
        ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
