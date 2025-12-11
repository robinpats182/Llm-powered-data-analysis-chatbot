# Llm-powered-data-analysis-chatbot
> Opinionated, demo-ready scaffold that lets people query CSV/SQL datasets in natural language and get **trustworthy**, **validated** analytics, tables, and charts.

![license](https://img.shields.io/badge/license-MIT-green) ![python](https://img.shields.io/badge/python-3.11-blue) ![fastapi](https://img.shields.io/badge/fastapi-%5E0.95-lightgrey)

## Tech stack

* Python 3.11
* FastAPI (REST API)
* Pandas, SQLite, SQLAlchemy (data operations)
* Matplotlib (charts)
* LangChain / LlamaIndex adapter-style + OpenAI/Mistral (LLM integration)
* Docker, docker-compose
* Pytest, GitHub Actions

---

## Architecture (ASCII diagram)

```
+-------------+      JSON tool-call       +------------+    Data ops    +---------+
|  User UI /  |  ----------------------->  |  LLM Agent | --------------> |  Tools  |
|  curl / UI  |                              (prompts)     run_sql/filter  | (CSV,   |
+-------------+                                |                          |  SQL,   |
                                               |  structured tool-call    | chart)  |
                                               v                          +---------+
                                            Executor
                                               |  (executes safe tools)
                                               |  Validator (parity checks)
                                               v
                                         Result formatter
                                               |
                                               v
                                           API response
```

Place a short animated GIF in the README showing a sample query -> chart generation (optional). Use `/artifacts/demo.gif` in the repo when you add it.

---

## README: Quickstart (for demo visitors)

1. Clone:

```bash
git clone https://github.com/<you>/llm-data-chatbot.git
cd llm-data-chatbot
cp .env.example .env            # add OPENAI_API_KEY or MISTRAL key
docker-compose up --build
```

2. Open the API docs: `http://localhost:8000/docs`
3. POST to `/api/v1/query` with JSON `{ "question": "Show monthly revenue trends and top 3 regions by revenue for 2024" }`

**1) Chain-of-thought safety** — The LLM is constrained to return *structured JSON tool-calls only*. The application never returns model chain-of-thought to users. This is enforced at the prompt layer and by a JSON parser that rejects non-conforming outputs.

**2) Deterministic tools** — All data operations are performed in small pure functions (CSVTool, SQLTool, ChartTool). This makes unit testing straightforward and reduces nondeterminism introduced by the model.

**3) Validation & reproducibility** — A `Validator` module re-runs aggregates where possible and performs numeric parity checks. Any mismatch is surfaced to the user along with the raw query and recomputed value.

**4) Token & context management** — The demo uses retrieval compression patterns for embedding-based retrieval and explicit `MAX_TOKENS`. The prompts compress context before sending to the LLM to reduce bills and avoid hallucinations.

**5) Security** — SQL execution is READ-ONLY and limited to `SELECT` statements. Inputs are sanitized and the demo runs on an isolated SQLite by default.

---

## API

* `GET /` — health check
* `POST /api/v1/query` — primary query endpoint (body: `{ question: str, top_k?: int }`).
* Artifacts served from `/artifacts` (chart images)

Add a tiny `curl` example in the README so hiring managers can try it without installing anything.

