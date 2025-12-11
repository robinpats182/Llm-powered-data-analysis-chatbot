from app.tools.db_tool import SQLTool


def test_select_returns_dataframe(tmp_path):
# create a temp sqlite and run
import sqlite3
db = tmp_path / "t.db"
conn = sqlite3.connect(db)
conn.execute("CREATE TABLE t (id INTEGER, v REAL);")
conn.execute("INSERT INTO t (id, v) VALUES (1, 2.0),(2,3.0);")
conn.commit()
conn.close()


tool = SQLTool(db_path=str(db))
df = tool.run_sql("SELECT * FROM t")
assert df.shape[0] == 2