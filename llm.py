from openai import OpenAI
from config import OPENAI_API_KEY

def call_llm(prompt:str) ->str:
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "API key da OpenAi não encontrada"
        )
    client = OpenAI(api_key = OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content