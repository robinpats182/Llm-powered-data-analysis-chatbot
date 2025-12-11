from fastapi import FastAPI
from app.api.v1 import router as api_router
from app.core.logger import logger


app = FastAPI(title="LLM Data Chatbot")


app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
def startup_event():
logger.info("Starting LLM Data Chatbot")


@app.get("/")
def index():
return {"ok": True, "message": "LLM Data Chatbot is running. Visit /docs"}