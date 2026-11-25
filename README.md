# AgroSugar-IoT · Avance 2

Virtualización KVM, contenedores Docker y orquestación Kubernetes (k3s) del caso AgroSugar.

- `Dockerfile`, `requirements.txt`, `app/`: imagen `agrosugar-ndvi:1.0` (multi-stage, python:3.11-slim, usuario no root).
- `k8s/`: `deployment.yaml`, `service.yaml`, `hpa.yaml`, `cronjob.yaml`.

Despliegue: `kubectl apply -f k8s/`
Validación: `kubectl apply --dry-run=client -f k8s/`

Entorno: Ubuntu 24.04 sobre VirtualBox, VM KVM `k8s-master`, k3s de un solo nodo.
