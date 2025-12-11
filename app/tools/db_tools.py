import sqlite3
import pandas as pd
from pathlib import Path


DB_PATH = Path(__file__).parent.parent / "models" / "sample.db"


class SQLTool:
def __init__(self, db_path: str | None = None):
self.db_path = db_path or DB_PATH


def run_sql(self, query: str) -> pd.DataFrame:
# Defensive: allow only SELECT queries
q = query.strip().lower()
if not q.startswith("select"):
raise ValueError("Only SELECT queries are allowed in this demo")
conn = sqlite3.connect(self.db_path)
try:
df = pd.read_sql_query(query, conn)
finally:
conn.close()
return df