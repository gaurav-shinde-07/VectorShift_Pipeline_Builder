# VectorShift Pipeline Builder

A small full‑stack application demonstrating a node-based pipeline builder with a neon Tailwind UI frontend and a FastAPI backend. The app provides an interactive ReactFlow canvas for composing pipelines and a backend DAG validator and dashboard accessible at /dashboard.

Status: Prototype — suitable as a foundation for productionization.

Table of contents
- Overview
- Highlights
- Repository layout
- Quick start
- Development
- Backend: dashboard & API
- Environment variables
- Scripts
- Testing
- Deployment notes
- Contributing
- License & contact

Highlights
----------
- Neon-themed Tailwind UI (responsive)
- ReactFlow-based drag-and-drop pipeline editor
- Node types: Math, API, Formatter, Logger, Conditional
- Backend DAG validation and small dashboard (FastAPI)
- Modular node engine designed for extension

Repository layout
----------------
VectorShift_Pipelines/
├─ frontend/           # React + Vite + Tailwind + ReactFlow UI  
│  ├─ src/             # components, pages, flows, stores  
│  ├─ public/  
│  ├─ package.json  
│  └─ tailwind.config.js  
├─ backend/            # FastAPI app, DAG validator, dashboard  
│  ├─ app/             # routes, services, validators  
│  ├─ main.py  
│  └─ requirements.txt  
├─ assets/             # images used in README or UI  
└─ README.md

Quick start
-----------
Prereqs:
- Node.js (LTS)
- npm or yarn
- Python 3.10+
- Git

1) Clone
   git clone https://github.com/gaurav-shinde-07/VectorShift_Pipeline_Builder
   cd VectorShift_Pipelines

2) Frontend (dev)
   cd frontend
   npm install
   npm run dev
   - Frontend default: http://localhost:5173

3) Backend (dev)
   cd backend
   python -m venv .venv
   source .venv/bin/activate   # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   uvicorn main:app --reload --port 8000
   - Backend: http://localhost:8000
   - Dashboard: http://localhost:8000/dashboard

Development
-----------
Frontend
- Start dev server: npm run dev
- Build: npm run build
- Lint / format: add/prefer ESLint + Prettier config as needed

Backend
- Run local server with uvicorn (see quick start)
- Add endpoints under backend/app/routes
- Unit tests: pytest (add tests/ folder)

Backend: dashboard & API
------------------------
- The dashboard endpoint (GET /dashboard) serves a small UI for inspecting pipelines / DAGs.
- API endpoints (example):
  - POST /validate — validate a submitted pipeline as DAG (uses NetworkX)
  - POST /execute — (prototype) run a pipeline locally (engine is modular and extensible)
- Consult backend/app for concrete routes and models.

Environment variables
---------------------
Create a .env in the appropriate folder (backend or root). Example:
PORT=8000
ENV=development
# Add external API keys or DB strings as required

Security: Never commit secrets.

Scripts (examples)
------------------
- frontend/package.json: dev, build, preview
- backend: run via uvicorn; consider adding a start script in package.json or Makefile

Testing
-------
- Frontend: add Jest / React Testing Library tests
- Backend: pytest for endpoints and validation logic

Contributing
------------
- Fork the repository and create a topic branch
- Keep commits focused and add tests for new behavior
- Open a PR with a description and rationale

Troubleshooting
---------------
- If the frontend cannot reach the backend, confirm CORS settings and ports
- Use uvicorn --reload during development to pick up backend changes

Acknowledgements
----------------
Built with React, ReactFlow, Tailwind CSS and FastAPI. Inspired by modern pipeline editors and node-based tools.
