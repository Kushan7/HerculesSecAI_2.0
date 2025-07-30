# Dockerfile (in project root)
FROM python:3.11-slim AS base

WORKDIR /app

# Only copy required files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy source code
COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
