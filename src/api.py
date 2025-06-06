from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline import run
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Response, Request
import logging


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    prompt: str


@app.post("/pipeline")
async def pipeline(request: PromptRequest):
    logging.info(f"Received request with prompt: {request.prompt}")
    result = await run(request.prompt)
    return {"result": result}
