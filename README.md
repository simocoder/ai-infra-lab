# ----------------------------
# README.md (outline)

# AI Infra Lab — Milestone 1: Local ML API with Docker + MLflow

This project trains a simple ML model, logs experiments with MLflow, and serves predictions through a FastAPI app in Docker.

## Features
- Train model using scikit-learn
- Log metrics and artifacts with MLflow
- Serve predictions via FastAPI
- Containerized with Docker

## Quick Start

1. Build and run:
```bash
docker build -t ai-infra-lab .
docker run -p 8000:8000 ai-infra-lab
```

2. Access API:
```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

3. Access MLflow UI:
```bash
mlflow ui
# then open http://localhost:5000
```
