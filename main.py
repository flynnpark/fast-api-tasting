from typing import Dict, List, Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results: Dict[str, Union[List[Dict[str, str]], str]] = {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]
    }
    if q:
        results.update({"q": q})
    return results
