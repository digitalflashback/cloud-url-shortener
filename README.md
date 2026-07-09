# Cloud URL Shortener

A cloud-native URL shortening application built to demonstrate modern DevOps and Cloud Engineering practices.

The application is deployed on Microsoft Azure using Docker containers, Azure Kubernetes Service, Terraform and GitHub Actions CI/CD.

## Project Overview

This project demonstrates the complete lifecycle of a cloud application:

- Application development
- Containerization with Docker
- Infrastructure provisioning with Terraform
- Container image management with Azure Container Registry
- Kubernetes deployment on Azure Kubernetes Service
- Automated deployment using GitHub Actions

## Architecture

The application consists of:

Frontend:
- React application
- Vite build system
- Docker container running on Kubernetes

Backend:
- REST API service
- Docker container running on Kubernetes

Infrastructure:
- Microsoft Azure
- Azure Kubernetes Service (AKS)
- Azure Container Registry (ACR)
- Terraform managed infrastructure

Database:
- PostgreSQL integration planned

## CI/CD Pipeline

The deployment process is fully automated.

When code is pushed to the main branch:

1. GitHub Actions starts the workflow.
2. Docker images are built.
3. Images are pushed to Azure Container Registry.
4. Kubernetes deployment is updated.
5. Kubernetes performs a rolling update.
6. Deployment status is verified.

Docker images use Git commit SHA tags to provide traceable and reproducible deployments.

## Infrastructure as Code

Azure resources are managed using Terraform.

The goal is to have a fully reproducible cloud environment that can be created and maintained through code.

Current Terraform-managed resources:

- Resource Group
- Azure Kubernetes Service
- Azure Container Registry
- Azure networking components

## Kubernetes Deployment

The application runs on Kubernetes using:

- Deployments
- Services
- Replica management
- Rolling updates
- Container health checks

The deployment process supports:

- Automated updates
- Version tracking
- Rollbacks

## Security

Implemented security practices:

- Azure RBAC
- GitHub Actions secrets
- Azure authentication
- Container Registry access control

Planned improvements:

- Azure Key Vault
- Managed Identity
- Kubernetes Secrets
- Network security policies

## DevOps Skills Demonstrated

This project demonstrates experience with:

- Microsoft Azure
- Kubernetes administration
- Docker containerization
- GitHub Actions CI/CD
- Terraform Infrastructure as Code
- Cloud deployment workflows
- Azure identity and access management

## Roadmap

Application improvements:

- URL creation API
- Short code generation
- Redirect service
- PostgreSQL persistence
- Click analytics

Cloud improvements:

- HTTPS ingress
- Custom domain
- Monitoring and alerting
- Prometheus and Grafana
- Automated testing pipeline
- Production approval workflow

## Project Goal

The goal of this project is to build and operate a production-style cloud-native application while demonstrating practical Cloud Engineering and DevOps capabilities.