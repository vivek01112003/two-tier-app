Two-Tier Flask Application using Docker
Project Overview

A two-tier web application developed using Python Flask and MySQL, containerized with Docker and managed using Docker Compose.

Technologies Used
Python
Flask
MySQL
Docker
Docker Compose
Linux
Git and GitHub
Architecture
Frontend/API Layer: Python Flask backend
Database Layer: MySQL database
Containerization: Docker
Orchestration: Docker Compose
Networking: Custom Docker bridge network
Storage: Docker named volume for persistent database data
Features
Flask API with JSON responses.
MySQL database connectivity check.
Separate backend and database containers.
Environment variables for database configuration.
Persistent database storage using Docker volumes.
Run the Project

Build the Docker image:

docker build -t two-tier-backend:latest .


Start the application:

docker compose up -d


Check containers:

docker compose ps


Stop the application:

docker compose down

Application Endpoints
http://localhost:8080/ — Check backend status.
http://localhost:8080/db — Check database connectivity.

Ensure Docker Compose maps port 8080 on the host to port 5000 in the Flask container.

Skills Demonstrated

Docker containerization, Docker Compose, Python Flask, MySQL connectivity, container networking, persistent storage, Linux basics, and GitHub version control.

Future Enhancements
Deploy on AWS EC2.
Use Amazon RDS for managed database hosting.
Implement CI/CD using GitHub Actions.
Add monitoring and secure secrets management.
Author
VIVEK SANADI - Cloud Engineer

Your Name
Aspiring Cloud Engineer | Python | Docker | Linux | AWS Fundamentals
