# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy backend files
COPY backend /app/backend
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
COPY .env /app/.env
COPY keys /app/keys

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
