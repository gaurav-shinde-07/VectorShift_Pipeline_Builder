from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Set
from fastapi.responses import HTMLResponse
import json
import datetime


# Application Setup

app = FastAPI(title="VectorShift Pipeline Validator + Dashboard")

# Enable CORS for front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Frontend uses localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Data Models

class Edge(BaseModel):
    source: str
    target: str

class Pipeline(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Edge]



# In-Memory Analytics Storage

analytics_store = {
    "total_requests": 0,
    "valid_dag": 0,
    "invalid_dag": 0,
    "history": []  # last 20 submissions
}



# DAG Validation Logic

def is_dag_with_checks(nodes: List[Dict[str, Any]], edges: List[Edge]) -> Dict[str, Any]:
    if not nodes or not isinstance(nodes, list):
        return {"isDAG": False, "error": "Nodes list is empty or invalid."}

    node_ids = [n.get("id") for n in nodes if "id" in n]
    if len(node_ids) != len(set(node_ids)):
        return {"isDAG": False, "error": "Duplicate node IDs detected."}

    if not edges:
        if len(nodes) == 1:
            return {"isDAG": True, "message": "Valid single-node DAG."}
        return {"isDAG": False, "error": "Edges list is empty or invalid."}

    adj = {nid: [] for nid in node_ids}
    seen_edges = set()

    for e in edges:
        if e.source not in adj or e.target not in adj:
            return {"isDAG": False, "error": f"Invalid edge: {e.source} -> {e.target}"}

        edge_pair = (e.source, e.target)
        if edge_pair in seen_edges:
            return {"isDAG": False, "error": f"Duplicate edge detected {edge_pair}"}

        seen_edges.add(edge_pair)
        adj[e.source].append(e.target)

    visited, stack = set(), set()

    def dfs(node: str) -> bool:
        if node in stack:
            return True
        if node in visited:
            return False
        visited.add(node)
        stack.add(node)
        for nei in adj.get(node, []):
            if dfs(nei):
                return True
        stack.remove(node)
        return False

    for n in adj:
        if dfs(n):
            return {"isDAG": False, "error": "Cycle detected in graph."}

    return {"isDAG": True, "message": "Valid DAG."}



# API Endpoint

@app.post("/pipelines/parse")
def parse_pipeline(pipeline: Pipeline):
    result = is_dag_with_checks(pipeline.nodes, pipeline.edges)

    # Update analytics
    analytics_store["total_requests"] += 1
    if result["isDAG"]:
        analytics_store["valid_dag"] += 1
    else:
        analytics_store["invalid_dag"] += 1

    analytics_store["history"].append({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nodes": len(pipeline.nodes),
        "edges": len(pipeline.edges),
        "result": result
    })

    analytics_store["history"] = analytics_store["history"][-20:]  # Keep last 20

    return result



# BACKEND DASHBOARD (HTML UI)

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    html = f"""
    <html>
    <head>
        <title>Backend Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                padding: 20px;
            }}
            .card {{
                background: #1e293b;
                padding: 20px;
                border-radius: 12px;
                width: 260px;
                display: inline-block;
                margin-right: 20px;
                box-shadow: 0 0 12px rgba(0, 200, 255, 0.3);
            }}
            table {{
                width: 100%;
                margin-top: 20px;
                border-collapse: collapse;
                background: #1e293b;
                color: #cbd5e1;
            }}
            th, td {{
                border: 1px solid #475569;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background: #334155;
            }}
        </style>
    </head>
    <body>
        <h1 style="color:#38bdf8;">VectorShift Backend Analytics Dashboard</h1>

        <div class="card">
            <h3>Total Requests</h3>
            <p style="font-size:24px;">{analytics_store["total_requests"]}</p>
        </div>

        <div class="card">
            <h3>Valid DAGs</h3>
            <p style="font-size:24px; color:#4ade80;">{analytics_store["valid_dag"]}</p>
        </div>

        <div class="card">
            <h3>Invalid DAGs</h3>
            <p style="font-size:24px; color:#f87171;">{analytics_store["invalid_dag"]}</p>
        </div>

        <canvas id="chart" height="120"></canvas>

        <script>
        const data = {{
            labels: ["Valid DAGs", "Invalid DAGs"],
            datasets: [{{
                data: [{analytics_store["valid_dag"]}, {analytics_store["invalid_dag"]}],
                backgroundColor: ["#4ade80", "#f87171"]
            }}]
        }};
        new Chart(document.getElementById("chart"), {{
            type: "doughnut",
            data: data
        }});
        </script>

        <h2 style="margin-top:40px;">Recent Submissions</h2>
        <table>
            <tr>
                <th>Time</th>
                <th>Nodes</th>
                <th>Edges</th>
                <th>Result</th>
            </tr>
            {''.join([
                f"<tr><td>{h['timestamp']}</td><td>{h['nodes']}</td><td>{h['edges']}</td><td>{'Valid' if h['result']['isDAG'] else 'Invalid'}</td></tr>"
                for h in analytics_store["history"]
            ])}
        </table>
    </body>
    </html>
    """

    return html


@app.get("/")
def home():
    return {"status": "Backend Running", "dashboard": "/dashboard"}
