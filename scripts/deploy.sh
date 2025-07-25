#!/bin/bash

# Move to project root directory
cd "$(dirname "$0")"/..

# Use Minikube's Docker daemon
eval $(minikube docker-env)

# Build Docker image from project root (where Dockerfile is)
docker build -t uptime-monitor:latest .

# Apply all Kubernetes manifests in k8s/ folder
kubectl apply -f k8s/

# Open the service in Minikube
minikube service uptime-monitor-service
