# AI Infra Lab — Milestone 1: Local ML API with Docker + MLflow

This project trains a simple ML model, logs experiments with MLflow, and serves predictions through a FastAPI app in Docker. **The Docker image now builds the model automatically, so you don’t have to run `train.py` manually.**

Uses the classic Iris flower dataset — one of the most widely used datasets in machine learning education.

🔍 Specifically, the load_iris function:

Returns 150 flower samples

Each with 4 features:

sepal length

sepal width

petal length

petal width

And a target label (0, 1, or 2) for the species:

0 = setosa

1 = versicolor

2 = virginica

In the code: 
```python
X, y = load_iris(return_X_y=True, as_frame=True)
```

X is a DataFrame with shape (150, 4) — the features

y is a Series with shape (150,) — the class labels

✅ This dataset lets you train a real model with no external data files, making it perfect for your local AI infra lab.

## Features
- Train model using scikit-learn (executed during Docker build)
- Log metrics and artifacts with MLflow
- Serve predictions via FastAPI
- Containerized with Docker

## Quick Start

```bash
# Clone repo and enter
git clone https://github.com/simocoder/ai-infra-lab.git
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
