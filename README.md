# VectorShift Assessment - Tailwind Pro

A frontend built with Tailwind CSS and a neon theme, paired with a backend that includes a small dashboard available at `/dashboard`. This README provides an overview, setup instructions, and a recommended project structure to help you run, develop, and deploy the project.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Typical Project Structure](#typical-project-structure)
- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
- [Environment Variables](#environment-variables)
- [Running the Dashboard](#running-the-dashboard)
- [Build & Production](#build--production)
- [Testing](#testing)
- [Contributing](#contributing)
- [License & Contact](#license--contact)


## Features
- 🎨 Neon-Themed Tailwind UI with responsive layout
- ⚡ ReactFlow-based Canvas for interactive drag-and-drop pipelines
- 🔢 Math Node with dynamic expression evaluation
- 🔗 API Node for external HTTP calls
- 🧪 Formatter Node for templated string output
- 🔍 Logger Node for debugging data flow
- 🔀 Conditional Node for branching logic
- 🧠 Backend DAG Validator using NetworkX
- 📊 Mini Dashboard at /dashboard (FastAPI)
- 🧱 Modular node engine ready for extension

## Tech Stack
# **Frontend**
- React + Vite  
- ReactFlow  
- Tailwind CSS (Neon theme)  
- Zustand (State Management) 

# **Backend**
- FastAPI  
- Python  
- NetworkX (DAG Validator)  
- Uvicorn  

## Project Structure
VectorShift_Pipelines/
│
├── frontend/               # React + Tailwind + ReactFlow UI
│   ├── src/
│   ├── public/
│   ├── tailwind.config.js
│   └── package.json
│
├── backend/                # FastAPI backend + DAG validation
│   ├── main.py
│   ├── requirements.txt
│   └── app/
│
├── assets/                 # Images for README
│
└── README.md


## Prerequisites
- Node.js (LTS recommended)
- npm or yarn
- Git 
- Python 3.10+

## Local Setup

1. Clone the repository
   - git clone https://github.com/gaurav-shinde-07/VectorShift_Pipeline_Builder
   - cd VectorShift_Pipelines

2. Frontend Setup
   - cd frontend
   - npm install
   - npm run dev
     
   - Frontend runs at
     - http://localhost:5173

3. Backend Setup
   - cd backend
   - pip install -r requirements.txt
   - uvicorn main:app --reload --port 8000

   - Backend runs at
    - http://localhost:8000
   - Dashboard :
    - http://localhost:8000/dashboard


## Environment Variables
Create a `.env` file in the relevant folder (backend or project root). 
```
PORT=8000
ENV=development
# Add API keys or DB connection strings as needed
```

## Testing
- npm test
- pytest

## Contributing
- Contributions are welcome!
- Fork the repo and create a feature branch
- Follow existing code style and add tests for new logic
- Open a pull request with a concise description of changes


---
