# Hello GoldenPath IDP

Lightweight test application for end-to-end build and deployment testing on the GoldenPath IDP platform.

## Quick Start

```bash
# Build locally
docker build -t hello-goldenpath-idp:v1 .

# Run
docker run -p 8080:8080 hello-goldenpath-idp:v1

# Test
curl http://localhost:8080
curl http://localhost:8080/health
curl http://localhost:8080/ready
```

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Hello message with version and environment |
| `/health` | Liveness probe |
| `/ready` | Readiness probe |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `8080` | Server port |
| `APP_VERSION` | `1.0.0` | Application version |
| `ENV` | `local` | Environment name |

## CI/CD

This repo includes a GitHub Actions workflow that:
1. Builds the Docker image
2. Pushes to Amazon ECR
3. Scans with Trivy for vulnerabilities

### Prerequisites

Set up the following GitHub secrets:
- `AWS_ROLE_ARN`: IAM role ARN for OIDC authentication

### ECR Repository

Request an ECR repository via the GoldenPath IDP Backstage portal using the ECR Request template.

## Backstage Integration

This component is registered in Backstage via `catalog-info.yaml`. To import:

1. Go to Backstage → Catalog → Import
2. Enter: `https://github.com/mikeybeezy/hello-goldenpath-idp/blob/main/catalog-info.yaml`

## Image Scanning Tests

To test vulnerability scanning, uncomment packages in `requirements.txt`:

```txt
requests==2.25.0      # CVE-2023-32681
urllib3==1.26.4       # CVE-2023-43804
```

Then rebuild and the CI pipeline will report findings.

## Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-goldenpath-idp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-goldenpath-idp
  template:
    metadata:
      labels:
        app: hello-goldenpath-idp
    spec:
      containers:
      - name: app
        image: <account-id>.dkr.ecr.us-east-1.amazonaws.com/hello-goldenpath-idp:latest
        ports:
        - containerPort: 8080
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
```
