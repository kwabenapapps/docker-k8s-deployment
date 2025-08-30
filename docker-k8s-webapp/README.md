# Docker & Kubernetes Web App

A minimal Flask service with health/readiness endpoints, containerized with Docker and deployable to Kubernetes (Minikube/EKS).

## Local (Docker)
```bash
docker build -t docker-k8s-webapp:latest .
docker run -p 8000:8000 -e APP_ENV=dev docker-k8s-webapp:latest
# or
docker compose up --build
```

Visit `http://localhost:8000/healthz`

## Minikube
```bash
minikube start
eval $(minikube -p minikube docker-env)
docker build -t docker-k8s-webapp:latest .

kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service -n webapp webapp-svc --url
minikube addons enable ingress
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml   # requires metrics-server
```
