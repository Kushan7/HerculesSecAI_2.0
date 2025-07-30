# Dockerfile (at project root)

FROM python:3.11-slim

WORKDIR /app

# Copy entire project into container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
