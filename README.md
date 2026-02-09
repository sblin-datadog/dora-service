# Dora Service

Simple Python service for DORA service demo.

## Endpoints

| Endpoint  | Method | Description                          |
|-----------|--------|--------------------------------------|
| `/dora`   | GET    | Returns "hi from dora-service"       |

## Build Docker Image

```bash
docker buildx build --platform linux/amd64 -t samuelblin/dora-service:1.0.0 .
```

## Push to Docker Hub

```bash
docker push samuelblin/dora-service:1.0.0
```

## Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
```

This will create:
- Namespace `dora`
- Deployment with 1 pod
- ClusterIP Service on port 80

## Environment Variables

| Variable     | Description              | Default         |
|--------------|--------------------------|-----------------|
| `DD_SERVICE` | Datadog service name     | `dora-service`  |
| `DD_VERSION` | Datadog version tag      | `1.0.0`         |
| `DD_ENV`     | Datadog environment tag  | `dev`           |
| `PORT`       | Application port         | `8080`          |

## Test Locally

```bash
# Run with Docker
docker run -p 8080:8080 samuelblin/dora-service:1.0.0

# Test endpoint
curl http://localhost:8080/dora
```

## Test on Kubernetes

```bash
kubectl port-forward -n dora svc/dora-service 8080:80
curl http://localhost:8080/dora
```

Version 1.1.0
Version 1.2.0
Version 1.3.0 
Version 1.4.0
Version 1.5.0
Version 1.5.1
Version 1.5.2
Version 1.7.0
Version 1.7.1
Version 1.7.2
