from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.get("/redirect")
async def handle_redirect(request: Request):
    token = request.query_params.get("request_token")
    if not token:
        return {"error": "Missing request_token"}

    print(f"[OAuth] request_token received: {token}")
    return {"status": "success", "message": "Token received. You may close this tab."}
