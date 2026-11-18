Flask Notes Manager – DevOps Project

Project Overview

A containerized Flask-based Notes Management application with PostgreSQL integration. This project demonstrates application deployment, CI/CD automation, Kubernetes orchestration, and monitoring using Prometheus and Grafana.

Technologies Used

Operating System: Linux (Ubuntu)

Programming: Python (Flask)

Database: PostgreSQL

Containerization: Docker, Docker Compose

Web Server: Nginx

CI/CD: GitHub Actions

Container Registry: Docker Hub

Orchestration: Kubernetes (Minikube)

Monitoring: Prometheus, Grafana

Version Control: Git, GitHub

Architecture

Developer → GitHub → GitHub Actions → Automated Testing → Docker Image → Docker Hub → Kubernetes Deployment → Flask Application → PostgreSQL

Prometheus collects application metrics, which can be visualized using Grafana.

Project Implementation

1. Application Development

Developed a Flask-based Notes Management application.

Integrated PostgreSQL for storing and managing notes.

Implemented application health-check functionality.

2. Docker Containerization

Created a Dockerfile to containerize the Flask application.

Configured Docker Compose to manage Flask, PostgreSQL, and Nginx services.

Configured Nginx as a reverse proxy for application traffic.

3. CI/CD Pipeline

Configured GitHub Actions for automated testing.

Automated Docker image building through the CI workflow.

Published Docker images to Docker Hub.

4. Kubernetes Deployment

Created Kubernetes Deployments for Flask and PostgreSQL.

Configured Kubernetes Services for application communication.

Used Secrets to manage PostgreSQL credentials.

Configured Persistent Volumes and Persistent Volume Claims for database storage.

Deployed and tested the application using Minikube.

5. Monitoring

Configured Prometheus to collect application metrics.

Integrated Prometheus metrics with Grafana for visualization.

Monitored application and container performance.

Key Learnings

Linux administration and command-line operations.

Docker containerization and multi-container management.

CI/CD pipeline automation using GitHub Actions.

Kubernetes Deployments, Services, Secrets and persistent storage.

Application monitoring using Prometheus and Grafana.

Git version control and Docker Hub image management.

Project Outcome

Successfully developed, containerized, and deployed a Flask Notes Management application using Docker and Kubernetes, implemented automated CI workflows, and explored application monitoring using Prometheus and Grafana.
