# QueryPilot AI — Multi‑Agent Data Intelligence System

## Overview

QueryPilot AI is a modular multi-agent system that answers complex user questions by combining structured database queries and real‑time web information. Agents collaborate: a SQL Agent fetches structured data, a Web Search Agent fetches recent web content, and an Analysis Agent combines both sources to produce insights.

Example user flow:
1. User: "Get Tesla revenue and latest news"
2. SQL Agent: Query the database for Tesla revenue
3. Web Search Agent: Retrieve recent Tesla news
4. Analysis Agent: Merge results and generate a summarized insight

## Architecture

User Query
   └─ Router / Main Controller
       ├─ SQL Agent → structured DB queries (MySQL)
       ├─ Web Search Agent → web information (search APIs)
       └─ Analysis Agent → aggregate & explain results

## Tech Stack
- Python 3.9+
- LangChain
- Groq LLM (Llama 3.1) or OpenAI (configurable)
- MySQL + SQLAlchemy
- dotenv for environment variable loading

## Features
- Natural language → SQL query generation
- Real-time web retrieval for recent events
- Multi-agent orchestration and analysis
- Modular structure: easily swap agents or LLMs

## Quick Example
Query:

Get Tesla revenue and latest news

Sample output (illustrative):

Tesla reported approximately $96.77B revenue in 2023. Recent news indicates Tesla continues expanding EV production globally. Insights: Tesla’s financial growth aligns with demand for EVs and international expansion.

---

## Installation (Windows / PowerShell)

Open PowerShell and run the following from the project root (the folder that contains `src`):

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

(If you use cmd.exe instead of PowerShell, run `.venv\Scripts\activate.bat`.)

2. Install dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

## Environment variables

Create a `.env` file in the project root with the required configuration. Example:

```env
GROQ_API_KEY=your_groq_api_key
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=your_database_name
```

Notes:
- Do not commit `.env` to source control. Use a secrets manager for production.
- The README and code assume these names; adjust in code if you rename them.

## Running the project

Run the main application from the project root so Python has package context:

```powershell
python -m src.main
```

Run a specific agent (recommended: run as a module so relative imports work):

```powershell
python -m src.agents.sql_agent
python -m src.agents.web_search_agent
```

Avoid executing source files directly like `python src\agents\sql_agent.py` because relative imports may fail that way; use `-m` or ensure the project root is on `PYTHONPATH`.

## Troubleshooting (common issues and fixes)

1. ImportError: attempted relative import with no known parent package
- Cause: running the file directly (no package context).
- Fix: run as a module: `python -m src.agents.sql_agent`

2. Import errors in the IDE but not in terminal
- Cause: IDE is using a different interpreter / venv than your terminal.
- Fix:
  - In PyCharm / IntelliJ: File > Settings > Project > Python Interpreter — set to the same interpreter shown by `python -c "import sys; print(sys.executable)"` in your terminal.
  - Mark `src/` as a Sources Root (right-click `src` > Mark Directory as > Sources Root).
  - Invalidate caches / restart IDE (File > Invalidate Caches / Restart).

3. `PromptTemplate` or LangChain import problems
- LangChain has changed package layout across versions. Try these imports in a Python REPL to see what works with your installed version:

```python
from langchain.prompts import PromptTemplate
# or
from langchain_core.prompts import PromptTemplate
```

If they fail, ensure you installed LangChain in the interpreter your IDE/terminal uses:

```powershell
pip install -U langchain
```

4. Type-checker yellow warnings (static/type warnings)
- These are warnings from your IDE's type checker (not always runtime errors). Common causes:
  - Type mismatch between what's passed and the function signature (example: SQLDatabase vs SQLDatabaseToolkit).
  - Missing type stubs or dynamically generated API surface the analyzer can’t introspect.
- Fixes:
  - Use the correct object expected by the API (create a SQLDatabaseToolkit when required).
  - Add `# type: ignore` to lines where the type system is too strict.
  - Configure your type checker (Pyright / mypy) or update the package that provides type stubs.

## Development tips
- When adding or testing code that uses relative imports, prefer `python -m package.module` from the project root.
- Keep secrets (API keys) out of source control; use `.env` for local dev and a secure store for production.
- If a new dependency causes import failures in the IDE, double-check the interpreter and reinstall packages into that environment.

## Next steps and improvements
- Add a router agent to orchestrate which tool(s) to call per query.
- Integrate LangGraph or a similar orchestration layer.
- Add vector search and a small Streamlit UI for interactive usage.

---

If you want, I can also:
- Add a simple `run.sh` / `run.ps1` to simplify common commands.
- Add a `requirements.txt` or update it if you want me to pin versions.
- Add a short CONTRIBUTING.md with development workflow.

If you want any of those, tell me which and I’ll add them.
