from fastapi import FastAPI, Request
import requests

from llm import call_llm
from prompts import *

app = FastAPI(title="Motor do sistema")


@app.get("/health")
def health():
    return {"status":"Ok","service":"backend"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api:app",
        host="localhost",
        port=8000,
        reload=True
    )