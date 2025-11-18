# VectorShift Pipeline Builder

A modern node-based pipeline builder with a neon Tailwind UI frontend and a FastAPI backend. Compose, validate and prototype data-processing pipelines using a drag‑and‑drop ReactFlow canvas; validate DAGs and inspect pipelines via a lightweight backend dashboard.

🚀 Features
- Interactive ReactFlow canvas for drag‑and‑drop pipeline creation
- Prebuilt node types: Math, API, Formatter, Logger, Conditional
- Real‑time validation of directed acyclic graphs (DAG) via NetworkX
- Neon-themed Tailwind UI with responsive layouts
- FastAPI backend with a small dashboard at /dashboard
- Modular engine designed for extension and integration

🛠️ Tech Stack
- Frontend: React + Vite, TypeScript, Tailwind CSS, ReactFlow, Zustand
- Backend: FastAPI, Python 3.10+, NetworkX, Uvicorn
- Optional: Docker for containerized deployment

📋 Prerequisites
- Node.js 18.x (LTS recommended)
- npm or yarn
- Python 3.10+
- Git

🔧 Installation & Quick Start
1. Clone
   git clone https://github.com/gaurav-shinde-07/VectorShift_Pipeline_Builder
   cd VectorShift_Pipelines

2. Frontend
   cd frontend
   npm install
   npm run dev
   - Dev server: http://localhost:5173

3. Backend
   cd backend
   python -m venv .venv
   source .venv/bin/activate     # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --reload --port 8000
   - API: http://localhost:8000
   - Dashboard: http://localhost:8000/dashboard

🔐 Environment Variables
Create a `.env` in backend or root. Example:
PORT=8000
ENV=development
# Add API keys or DB connection strings as needed
Never commit secrets.

⚙️ Running & Development
- Frontend: npm run dev, build: npm run build
- Backend: uvicorn main:app --reload --port $PORT
- Consider adding linting (ESLint/Prettier) and tests (Jest, pytest)

📡 API & Dashboard
- GET /dashboard — serves the dashboard UI
- POST /validate — validate submitted pipeline graph (DAG check)
- POST /execute — (prototype) run pipeline using modular node engine
Check backend/app for routes and models.

🧪 Testing
- Frontend: Add Jest/RTL tests
- Backend: pytest — add tests/ to validate DAG logic and endpoints

📦 Deployment Notes
- Frontend: Vercel, Netlify, or static hosting after build
- Backend: Containerize and deploy to Cloud Run, ECS, or similar ASGI host
- Use host secret managers for environment variables

🤝 Contributing
- Fork repo, create feature branch, add focused commits and tests
- Open a PR with a clear description and rationale


👥 Authors & Contact
Gaurav Shinde — initial work  
For issues or questions: create a GitHub issue or email gauravmshinde017@gmail.com

🙏 Acknowledgements
Built with React, ReactFlow, Tailwind CSS and FastAPI. Inspired by modern pipeline editors and node‑based tooling.

🚀 Preview 

![Pipeline Builder Preview](./.assets/vect.png)

---
