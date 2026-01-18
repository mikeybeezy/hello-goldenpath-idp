FROM python:3.12-alpine

LABEL maintainer="platform-team"
LABEL version="1.0.0"
LABEL description="GoldenPath IDP test application"

WORKDIR /app

# Add requirements (empty for now, add deps later for scanning tests)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
