Cloud URL Shortener ☁️

A cloud-native URL shortening platform built to demonstrate modern DevOps and Cloud Engineering practices.

The project includes a containerized frontend and backend application deployed on Microsoft Azure Kubernetes Service (AKS) with automated CI/CD, Infrastructure as Code, and cloud-native deployment workflows.

Architecture Overview

                 User
                  |
                  |
            Azure Load Balancer
                  |
                  |
              Kubernetes
                  |
        +---------+---------+
        |                   |
        |                   |
   Frontend Pod        Backend Pod
   React + Nginx       API Service
        |                   |
        |                   |
        +---------+---------+
                  |
             PostgreSQL

Technology Stack
Application
Frontend
React
Vite
Nginx
Docker
Backend
API service
Docker
REST API architecture
Database
PostgreSQL (planned integration)
Cloud Infrastructure
Microsoft Azure

The application is deployed on Azure Kubernetes Service (AKS).

Infrastructure components:

Azure Kubernetes Service (AKS)
Azure Container Registry (ACR)
Azure Resource Groups
Azure Networking
Azure Container Instances (development/testing)

Infrastructure is managed using Terraform.

Kubernetes Deployment

The application runs inside Kubernetes with:

Deployments
Services
Rolling updates
Replica management
Container health management

Example deployment flow:

New Docker Image
        |
        |
Azure Container Registry
        |
        |
kubectl set image
        |
        |
Kubernetes Rolling Update
        |
        |
New Application Version
CI/CD Pipeline

Automated deployment is implemented using GitHub Actions.

Pipeline workflow:

Git Push
   |
   |
GitHub Actions
   |
   |
Docker Build
   |
   |
Push Image to ACR
   |
   |
Authenticate with Azure
   |
   |
Deploy to AKS
   |
   |
Verify Kubernetes Rollout

Features:

Automated Docker image builds
Container Registry integration
Kubernetes deployment
Rolling deployment verification
Immutable image tags using Git commit SHA
Infrastructure as Code

Terraform is used to provision Azure resources.

Example:

terraform/
 |
 └── azure/
      |
      ├── providers.tf
      ├── main.tf
      ├── variables.tf
      └── outputs.tf

Infrastructure can be recreated using:

terraform init

terraform plan

terraform apply
Security

Implemented security practices:

Azure RBAC
Service Principal authentication
GitHub Actions secrets
Container Registry access control
Kubernetes authentication using Azure AD

Planned improvements:

Azure Key Vault integration
Managed Identity
Kubernetes Secrets management
Network security policies

Deployment

Build locally

Frontend:

cd frontend

npm install

npm run build

Backend:

cd backend

docker build -t url-shortener-api .

Kubernetes Commands

Check deployments:

kubectl get deployments

Check pods:

kubectl get pods

Check services:

kubectl get services

Check rollout:

kubectl rollout status deployment/url-shortener-api

Rollback:

kubectl rollout undo deployment/url-shortener-api

Current Features

✅ Containerized frontend
✅ Containerized backend
✅ Azure Container Registry
✅ Azure Kubernetes Service deployment
✅ GitHub Actions CI/CD
✅ Automated Docker builds
✅ Kubernetes rolling deployments
✅ Infrastructure managed with Terraform

Roadmap
Application
URL creation API
Short code generation
Redirect endpoint
PostgreSQL integration
Click analytics
Cloud / DevOps
Azure Key Vault
Managed Identity
Kubernetes Secrets
Ingress Controller
HTTPS/TLS
Monitoring and alerting
Prometheus + Grafana
Automated testing pipeline
Project Goal

This project was created as a practical Cloud Engineering portfolio project to demonstrate:

Cloud infrastructure design
Kubernetes operations
CI/CD automation
Infrastructure as Code
Container orchestration
Azure platform engineering

The goal is to build and operate a production-style cloud-native application following modern DevOps principles.