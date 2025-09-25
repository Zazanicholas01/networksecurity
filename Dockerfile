FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies first (efficient caching)
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
