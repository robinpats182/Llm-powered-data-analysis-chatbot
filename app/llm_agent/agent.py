import json
import asyncio
from typing import Any
from app.core.config import settings
from app.core.logger import logger
from app.llm_agent.prompts import TOOL_INSTRUCTION
from app.tools.db_tool import SQLTool
from app.tools.csv_tool import CSVTool
from app.tools.chart_tool import ChartTool
from app.llm_agent.validation import Validator


# Note: this agent is intentionally simple and deterministic. Replace the `call_model` method
# with your LangChain or direct OpenAI/Mistral API calls.


class LLMAgent:
def __init__(self):
self.sql = SQLTool()
self.csv = CSVTool()
self.chart = ChartTool()


async def call_model(self, prompt: str) -> str:
"""Stub for model call. Replace with proper LLM invocation.
It must return the LLM text output (expected to be a JSON tool call or final summary).
"""
# For demo/testing we map a few canned prompts
if "monthly revenue" in prompt.lower():
return json.dumps({"tool": "run_sql", "query": "SELECT month, SUM(revenue) as revenue FROM sales GROUP BY month ORDER BY month"})
return json.dumps({"tool": "noop"})


async def handle_user_query(self, question: str, top_k: int = 5) -> dict:
prompt = TOOL_INSTRUCTION + "\nUser: " + question
logger.info("Sending prompt to model")
raw = await self.call_model(prompt)


# Expect JSON describing tool call
try:
payload = json.loads(raw)
except json.JSONDecodeError:
return {"error": "LLM returned non-JSON response", "raw": raw}


if payload.get("tool") == "run_sql":
query = payload.get("query")
df = self.sql.run_sql(query)
# Basic validation: if an aggregate was requested, validate parity if possible
# Example: if sum(revenue) exists we can re-run and compare
result = {"type": "table", "columns": list(df.columns), "rows": df.head(100).to_dict(orient="records")}
# produce a chart image path
chart_path = self.chart.line_plot(df, x=df.columns[0], y=df.columns[1], title=question)
summary = f"Returned {len(df)} rows. Generated chart at: {chart_path}"
return {"result": result, "chart": chart_path, "summary": summary}


return {"message": "No-op or unrecognized tool"}