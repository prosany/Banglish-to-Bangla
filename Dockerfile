# Use latest Python image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy files
COPY . .

# Upgrade pip first (important!)
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 7077

# Run FastAPI server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7077"]
