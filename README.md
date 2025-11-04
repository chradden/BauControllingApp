
# 🧱 Bau-Controlling App (DIN 276 + Fördermittel-Nachweis)

MVP-Scaffold für FastAPI (Backend) + React/Vite (Frontend).  
Ziel: Bauantrag → Budget (DIN 276) → Vergabe → Rechnungsprüfung → Zahlung → Schlussverwendungsnachweis.

## Quickstart (Codespaces)
1. **Python Backend**
   ```bash
   cd backend
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   cp ../.env.example .env  # oder eigene Variablen setzen
   uvicorn app.main:app --reload --port 8000
   ```
   Healthcheck: http://localhost:8000/health | Docs: http://localhost:8000/docs

2. **Frontend**
   ```bash
   cd frontend
   npm install
   npm run dev -- --port 5173
   ```
   UI: http://localhost:5173

## Struktur
```
backend/  -> FastAPI + SQLAlchemy
frontend/ -> React + Vite + TypeScript
docs/     -> prd.md, todo.md, Logs
scripts/  -> Hilfsskripte
```
