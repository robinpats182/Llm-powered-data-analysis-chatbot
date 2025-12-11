from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.llm_agent.agent import LLMAgent


router = APIRouter()
agent = LLMAgent()


class QueryRequest(BaseModel):
question: str
top_k: int = 5


@router.post("/query")
async def query(request: QueryRequest = Body(...)):
# synchronous / simple interface
response = await agent.handle_user_query(request.question, top_k=request.top_k)
return response