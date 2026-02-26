# Containerized Python Web App with Redis Backend

## 🏗 Project Overview
This project demonstrates a containerized two-tier web application using Python (Flask) and a Redis caching layer. It serves as the foundational microservice architecture for my 90-day transition into Platform Engineering / SRE.

## 🧠 Architecture
Instead of using basic Docker setups, this project implements production-grade containerization practices:
- **Multi-Stage Builds:** The Python `Dockerfile` utilizes a multi-stage approach. Dependencies are built in a heavy image and only the compiled artifacts are copied to a lightweight production image (e.g., `python:3.9-slim`). 
- **Security & Optimization:** This drastically reduces the attack surface by stripping out build tools and significantly reduces the image size, leading to faster pull times in CI/CD pipelines and Kubernetes nodes.
- **Network Isolation:** The application runs on a custom Docker bridge network via `docker-compose`, ensuring the Redis backend is not exposed directly to the host network, mimicking a private subnet architecture.

## 🛠 Tech Stack
* **Language:** Python 3.12 (Flask)
* **Backend/Cache:** Redis
* **Containerization:** Docker, Docker Compose
* **Orchestration:** Kubernetes (`kind`)

## 🚀 How to Run Locally

### Prerequisites
* Docker and Docker Compose installed on your machine.

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshpatel02/two-tier-app.git
   cd two-tier-app
2. **Run python app.py**