# stack-ai-assignment
Assignment provided by Antoni from Stack-AI

Link to the assignment: https://stack-ai.notion.site/Take-at-Home-Task-Backend-Vector-DB-bff06d35e031498fb6469875a40adeea

# Vector Database API

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Usage](#usage)
   - [Running the Application](#running-the-application)
   - [Testing the API](#testing-the-api)
7. [Deployment](#deployment)
   - [Docker](#docker)
   - [Kubernetes](#kubernetes)
8. [Future Improvements](#future-improvements)
---

## Introduction

This project implements a **Vector Database API** that allows users to index and query their documents within a vector database. The API supports CRUD operations for libraries, documents, and chunks, and provides efficient k-Nearest Neighbor (k-NN) searches using custom indexing algorithms. The application is containerized using Docker and can be deployed on a Kubernetes cluster.

---

## Features

- **CRUD Operations**: Create, Read, Update, and Delete libraries, documents, and chunks.
- **Indexing**: Build indexes for libraries using custom algorithms (Linear Search, KD-Tree, Ball Tree).
- **k-NN Search**: Perform efficient k-Nearest Neighbor searches on indexed libraries.
- **Concurrency Handling**: Ensures thread-safe operations using read-write locks.
- **Containerization**: The application is packaged in a Docker container.
- **Kubernetes Deployment**: The application can be deployed on a Kubernetes cluster using Helm.

---

## Tech Stack

- **Backend**: Python, FastAPI, Pydantic
- **Indexing Algorithms**: Linear Search, KD-Tree, Ball Tree
- **Containerization**: Docker
- **Deployment**: Kubernetes, Helm
- **Concurrency**: `threading.Lock`

---

## Project Structure

```
stack-ai-assignment/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── libraries.py  # Library-related endpoints
│   │   │   ├── documents.py  # Document-related endpoints
│   │   │   ├── chunks.py     # Chunk-related endpoints
│   │   │   └── indexing.py   # Indexing-related endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── library.py    # Library class
│   │   │   ├── document.py   # Document class
│   │   │   └── chunk.py      # Chunk class
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── library_service.py  # Library service
│   │   │   ├── document_service.py # Document service
│   │   │   └── chunk_service.py    # Chunk service
│   │   └── indexing/
│   │       ├── __init__.py
│   │       ├── base.py       # Base indexing class
│   │       └── algorithms/   
│   │           ├── __init__.py
│   │           ├── linear_search.py
│   │           ├── kd_tree.py
│   │           └── ball_tree.py
│   └── utils/
│       ├── __init__.py
│       └── concurrent.py     # Concurrency handling
├── deployment/
│   └── helm/               # Kubernetes deployment files
├── requirements.txt
├── Dockerfile           # Docker configuration
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.8+
- Docker
- Kubernetes (Minikube or a cloud provider like GKE)
- Helm

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/vector-db.git
   cd vector-db
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Application

1. **Run Locally**:
   ```bash
   uvicorn src.api.main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

2. **Access the Swagger UI**:
   Open your browser and go to `http://localhost:8000/docs` to interact with the API.

---

### Testing the API

#### Example Requests

1. **Create a Library**:
   - **Endpoint**: `POST /libraries/`
   - **Request Body**:
     ```json
     {
       "id": "lib1",
       "documents": [],
       "metadata": {}
     }
     ```

2. **Index the Library**:
   - **Endpoint**: `POST /indexing/index/lib1?algorithm=linear_search`

3. **Search the Library**:
   - **Endpoint**: `POST /indexing/search/lib1`
   - **Request Body**:
     ```json
     {
       "query_embedding": [0.1, 0.2, 0.3],
       "k": 2
     }
     ```

---

## Deployment

### Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t vector-db-api .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 8000:80 vector-db-api
   ```

   The API will be available at `http://localhost:8000`.

---

### Kubernetes

1. **Deploy the Helm Chart**:
   ```bash
   helm install vector-db ./deployment/helm/vector-db
   ```

2. **Verify the Deployment**:
   ```bash
   kubectl get pods
   ```

3. **Access the Application**:
   - Use `kubectl port-forward` to access the application:
     ```bash
     kubectl port-forward svc/vector-db 8000:80
     ```
   - Open your browser and go to `http://localhost:8000/docs`.

---

## Future Improvements

1. **Persistence**:
   - Add support for persistent storage (e.g., SQLite, PostgreSQL, or MongoDB).
   - Implement periodic saving of data to disk.

2. **Metadata Filtering**:
   - Enhance the search functionality to support metadata filtering.

3. **Python SDK**:
   - Develop a Python SDK to simplify API interactions.

4. **Leader-Follower Architecture**:
   - Implement a leader-follower architecture for scalability and high availability.

5. **Monitoring and Logging**:
   - Integrate monitoring tools like Prometheus and Grafana.
   - Add logging using ELK Stack or Loki.

6. **CI/CD Pipeline**:
   - Set up a CI/CD pipeline using GitHub Actions or Jenkins.

7. **Security**:
   - Implement authentication and authorization (e.g., OAuth2 or JWT).
   - Secure the API using HTTPS.