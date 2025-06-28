from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, PlainTextResponse
import json
import uuid

app = FastAPI()

temp_storage = {}

@app.get("/redirect")
async def display(request: Request):
    query_params = dict(request.query_params)

    if not query_params:
        return PlainTextResponse("No query parameters found", status_code=400)

    key = str(uuid.uuid4())
    temp_storage[key] = query_params
    return RedirectResponse(url=f"/result/{key}")

@app.get("/result/{key}", response_class=PlainTextResponse)
async def result(key: str):
    data = temp_storage.pop(key, None)  # Pop to delete after first access
    if data is None:
        return PlainTextResponse("Data not found or expired", status_code=404)

    pretty = json.dumps(data, indent=4, sort_keys=True)
    return pretty