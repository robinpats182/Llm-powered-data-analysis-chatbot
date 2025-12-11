import matplotlib.pyplot as plt
from pathlib import Path


OUT_DIR = Path(__file__).parent.parent.parent / "artifacts"
OUT_DIR.mkdir(exist_ok=True)


class ChartTool:
def line_plot(self, df, x: str, y: str, title: str = "") -> str:
# NOTE: do not set colors or styles; keep matplotlib defaults
fig, ax = plt.subplots()
ax.plot(df[x], df[y])
ax.set_title(title)
ax.set_xlabel(x)
ax.set_ylabel(y)
out_path = OUT_DIR / f"chart-{abs(hash(title)) % (10**8)}.png"
fig.savefig(out_path, bbox_inches='tight')
plt.close(fig)
return str(out_path)