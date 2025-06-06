from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline import run
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/pipeline")
async def pipeline(request: PromptRequest):
    result = await run(request.prompt)
    return {"result": result}