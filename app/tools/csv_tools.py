import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).parent.parent.parent / "data"


class CSVTool:
def __init__(self, base_path: Path | None = None):
self.base_path = base_path or DATA_DIR


def read(self, name: str) -> pd.DataFrame:
p = self.base_path / name
return pd.read_csv(p)


def filter(self, df: pd.DataFrame, filters: dict) -> pd.DataFrame:
# filters: {col: value} supports simple equality and ranges as tuples
out = df
for k, v in filters.items():
if isinstance(v, (list, tuple)) and len(v) == 2:
out = out[(out[k] >= v[0]) & (out[k] <= v[1])]
else:
out = out[out[k] == v]
return out