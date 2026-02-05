from fastapi import FastAPI, Request
import requests

from llm import call_llm
from prompts import *

app = FastAPI(title="Motor do sistema")


@app.get("/health")
def health():
    return {"status":"Ok","service":"backend"}

@app.post("/ai/beginner")
async def ai_beginner(request:Request):
    data = await request.json()
    situation = data.get("situation","")
    
    if not situation:
        return {"error":"Nenhuma situação enviada"}

    prompt = build_prompt_beginner(situation) 
    answer = call_llm(prompt)
    return {"mode":"beginner",
            "answer":answer}

@app.post("/ai/advanced")
async def ai_advanced(request:Request):
    data = await request.json()
    situation = data.get("situation","")

    if not situation:
        return {"error":"Nehuma situação enviada"}
    
    prompt = build_prompt_advanced(situation)
    answer = call_llm(prompt)
    return {"mode":"advanced",
            "answer":answer}

@app.post("/ai/trustable")
async def ai_trustable(request:Request):
    data = await request.json()
    situation = data.get("situation","")
    
    if not situation:
        return {"error":"Nehuma situação enviada"}
    
    prompt = build_prompt_very_trustable(situation)
    answer = call_llm(prompt)
    return {"mode":"trustable",
            "answer":answer}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api:app",
        host="localhost",
        port=8000,
        reload=True
    )