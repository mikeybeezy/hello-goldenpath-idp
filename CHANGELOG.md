# Changelog

All notable changes to the hello-goldenpath-idp project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-01-21

### Added
- Initial release as the standard stateless demo application for Golden Path IDP
- Flask-based Python web application with health and readiness endpoints
- Kong Ingress configuration for `hello-goldenpath-idp.dev.goldenpathidp.io`
- Kustomize-based deployment with overlays for dev, staging, test, and prod
- GitHub Actions delivery workflow
- Pre-commit hooks configuration
- Unit tests with pytest

### Infrastructure
- Kubernetes Deployment with resource limits and health probes
- ClusterIP Service on port 80
- Kong Ingress with wildcard DNS support via `*.dev.goldenpathidp.io`
- ECR image repository at `593517239005.dkr.ecr.eu-west-2.amazonaws.com/hello-goldenpath-idp`

### Branch Protection
- `main` branch: Requires PR with 1 approval, no force push, no deletion
- `development` branch: No force push, no deletion

### Endpoints
- `GET /` - Main page with interactive background toggle
- `GET /health` - Liveness probe endpoint
- `GET /ready` - Readiness probe endpoint

## Repository Info

- **Repository**: https://github.com/mikeybeezy/hello-goldenpath-idp
- **Branches**: `main` (protected), `development` (protected)
- **CI/CD**: ArgoCD with Image Updater
- **Access URL**: http://hello-goldenpath-idp.dev.goldenpathidp.io

---

This application serves as the reference implementation for stateless applications
deployed on the Golden Path IDP platform.
