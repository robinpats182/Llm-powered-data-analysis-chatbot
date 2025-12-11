# Structured tool-call prompt template. Keep minimal, deterministic.
import pandas as pd
TOOL_INSTRUCTION = ""

from app.core.logger import logger


class Validator:
@staticmethod
def numeric_parity_check(original: float, recomputed: float, tol: float = 1e-6) -> bool:
# returns True if within tolerance
ok = abs(original - recomputed) <= max(tol, abs(original) * 1e-6)
if not ok:
logger.warning(f"Parity check failed: original={original} recomputed={recomputed}")
return ok


@staticmethod
def validate_aggregates(table: pd.DataFrame, agg_column: str, expected_total: float) -> bool:
recomputed = float(table[agg_column].sum())
return Validator.numeric_parity_check(expected_total, recomputed)