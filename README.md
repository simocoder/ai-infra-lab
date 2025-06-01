
# ----------------------------
# README.md (outline)

# AI Infra Lab — Milestone 1: Local ML API with Docker + MLflow

This project trains a simple ML model, logs experiments with MLflow, and serves predictions through a FastAPI app in Docker. **The Docker image now builds the model automatically, so you don’t have to run `train.py` manually.**

## Features
- Train model using scikit-learn (executed during Docker build)
- Log metrics and artifacts with MLflow
- Serve predictions via FastAPI
- Containerized with Docker

## Quick Start

```bash
# Clone repo and enter
git clone https://github.com/your-user/ai-infra-lab.git
cd ai-infra-lab

# Build image — this runs train.py and creates model/model.pkl
docker build -t ai-infra-lab .

# Run API
docker run -p 8000:8000 ai-infra-lab

# Call the API
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# Optional: launch MLflow UI locally (outside container)
mlflow ui --backend-store-uri ./mlruns
```
